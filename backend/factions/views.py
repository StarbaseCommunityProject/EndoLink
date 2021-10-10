from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import ScopedRateThrottle
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .serializers import FactionSerializer, FactionCreationSerializer
from .models import Faction, FactionMember

# Create your views here.


class FactionCreationView(GenericAPIView):
    """
    Create Faction

    API endpoint to create a new faction as a user.

    Will only work if the user is not already in a faction.

    This route is intended to be used for faction creation by regular users.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'faction'
    serializer_class = FactionCreationSerializer
    filter_backends = []
    pagination_class = None

    @swagger_auto_schema(responses={200: FactionSerializer(many=False)}, operation_id='create_faction', tags=["factions"])
    def post(self, request):
        serializer = FactionCreationSerializer(data=request.data)
        response = dict()

        if serializer.is_valid():
            if Faction.objects.filter(leader=request.user).count() == 0 and FactionMember.objects.filter(user=request.user).count() == 0:
                new_faction = serializer.save(leader=request.user)
                response['faction'] = new_faction
                response_status = status.HTTP_201_CREATED
            else:
                response_status = status.HTTP_400_BAD_REQUEST
        else:
            response = serializer.errors
            response_status = status.HTTP_400_BAD_REQUEST

        return Response(response, status=response_status)

    def options(self, request, *args, **kwargs):
        meta = self.metadata_class()
        data = meta.determine_metadata(request, self)
        return Response(data=data, status=status.HTTP_200_OK)

