from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers
from django.db.models import Count
from .models import ShipEntry, ShipImage, ShipLike, ShipWishlist
from .forms import ShipCreationForm
import json

# Create your views here.


def clean_serialized_data(ser_data, dump=False):
    data = json.loads(ser_data)
    for entry in data:
        del entry['model']
        # In case we also want to remove the primary key from the data:
        # del entry['pk']
    if dump:
        return json.dumps(data)
    return data


def catalogue(request):
    ships = ShipEntry.objects.all()
    return HttpResponse(render(request, 'shipshop/catalogue.html', {'ships': ships}))


def ship_search(request):
    """
    Example query: http://localhost:8000/ship_search?search=centauri&tags=miner,long+range,Mining+Laser&attributes=speed:100,cargo%20crates:200&sort=updated&page=1&entries_per_page=5
    TODO: Needs some more sanitising of query inputs & error catching.
    :param request: Request data
    :return: JSON object containing query information and found ships.
    """
    search_term = request.GET.get('search') or None                 # "search term"
    tags = request.GET.get('tags') or None                          # [tag1, tag2, ...]
    attributes = request.GET.get('attributes') or None              # {'attribute': value, ...}
    updated_after = request.GET.get('updated_after') or None        # datetime string TODO
    sort = request.GET.get('sort') or None                          # "update"/"likes"/"alphabetical"
    page_nr = request.GET.get('page') or 1                          # 1
    entries_per_page = request.GET.get('entries_per_page') or 10    # 10

    return_all = True
    ships = ShipEntry.objects.filter(is_public=True).filter(is_deleted=False)
    if search_term:
        return_all = False
        ships = ships.filter(ship_name__unaccent__icontains=search_term)
    if tags:
        return_all = False
        tags = tags.split(",")
        for tag in tags:
            ships = ships.filter(tags__icontains=tag)
    if attributes:
        return_all = False
        attributes = attributes.split(",")
        for attribute in attributes:
            try:
                key, value = attribute.split(":")
                ships = ships.filter(attributes__contains=json.loads(f"{{\"{key}\":{value}}}"))
            except Exception as e:
                print(e)
    if return_all:
        ships = ships.all()

    ships = ships.annotate(likes_count=Count('shiplike'))

    if sort:
        if sort.lower() == "update":
            ships = ships.order_by('-updated_at')
        elif sort.lower() == "likes":
            ships = ships.order_by('-likes_count')
        elif sort.lower() == "alphabetical":
            ships = ships.order_by('ship_name')
        else:
            ships = ships.order_by('-created_at')
    else:
        ships = ships.order_by('-created_at')

    try:
        entries_per_page = max(int(entries_per_page), 1)
    except ValueError:
        entries_per_page = 10
    paginator = Paginator(ships, entries_per_page)

    try:
        exception_test = paginator.page(page_nr)
    except PageNotAnInteger:
        page_nr = 1
    except EmptyPage:
        page_nr = paginator.num_pages

    ship_count = len(ships)
    page_nr = int(page_nr)
    ships = paginator.page(page_nr)
    ship_count_this_page = len(ships)

    ships = serializers.serialize('json', ships)
    result = {'page': page_nr, 'total_pages': paginator.num_pages, 'total_entries': ship_count, 'total_entries_on_page': ship_count_this_page, 'ships': clean_serialized_data(ships), 'query': {'search_term': search_term, 'tags': tags, 'attributes': attributes, 'sort': sort, 'page': page_nr, 'entries_per_page': entries_per_page}}
    return JsonResponse(result)


@login_required
def ship_creation(request):
    form = ShipCreationForm(request.POST)
    if form.is_valid() and request.POST:
        ship = form.save(commit=False)
        ship.creator = request.user
        ship.save()

        for image in request.FILES.getlist("images_upload"):
            new_ship_image = ShipImage(image=image)
            new_ship_image.save()
            ship.images.add(new_ship_image)

    return HttpResponse(render(request, 'shipshop/ship_creation.html', {'form': form}))


@login_required
def like_ship(request, ship_id):
    response = {'success': False}
    if ShipLike.objects.filter(user=request.user, liked_ship_id=ship_id).first():
        return JsonResponse(response)

    ship = ShipEntry.objects.filter(id=ship_id).first()
    if not ship:
        return JsonResponse(response)

    new_ship_like = ShipLike(user=request.user, liked_ship=ship)
    try:
        new_ship_like.save()
        response = {'success': True}
    except Exception as e:
        response["exception"] = e.args[0]

    return JsonResponse(response)


@login_required
def unlike_ship(request, ship_id):
    response = {'success': False}
    ship_like = ShipLike.objects.filter(user=request.user, liked_ship_id=ship_id).first()
    if not ship_like:
        return JsonResponse(response)

    if ship_like.delete():
        response = {'success': True}

    return JsonResponse(response)


@login_required
def wishlist_ship(request, ship_id):
    response = {'success': False}
    if ShipWishlist.objects.filter(user=request.user, wishlisted_ship_id=ship_id).first():
        return JsonResponse(response)

    ship = ShipEntry.objects.filter(id=ship_id).first()
    if not ship:
        return JsonResponse(response)

    new_ship_wishlist = ShipWishlist(user=request.user, wishlisted_ship=ship)
    try:
        new_ship_wishlist.save()
        response = {'success': True}
    except Exception as e:
        response["exception"] = e.args[0]

    return JsonResponse(response)


@login_required
def unwishlist_ship(request, ship_id):
    response = {'success': False}
    ship_wishlist = ShipWishlist.objects.filter(user=request.user, wishlisted_ship_id=ship_id).first()
    if not ship_wishlist:
        return JsonResponse(response)

    if ship_wishlist.delete():
        response = {'success': True}

    return JsonResponse(response)


@login_required
def wishlist(request):
    wishlisted_ships = ShipWishlist.objects.filter(user=request.user)
    result = serializers.serialize('json', wishlisted_ships, fields='wishlisted_ship')

    return JsonResponse({'user_id': request.user.id, 'wishlisted_ships': clean_serialized_data(result)})


@login_required
def likes(request):
    liked_ships = ShipLike.objects.filter(user=request.user)
    result = serializers.serialize('json', liked_ships, fields='liked_ship')

    return JsonResponse({'user_id': request.user.id, 'liked_ships': clean_serialized_data(result)})
