# StarbaseCommunityWebsite
An open-source Starbase community website.

## How to run:

Docker Compose should take care of everything and automatically build the containers & run the webserver.

In case you want to run the webserver without Docker (not recommended), you can simply run `python manage.py runserver` in the `Project` directory. Be sure to install the necessary requirements from `Project/requirements.txt` first, though.


## Current Django Apps:

- Index

    The Index app is currently just the index page. See the `index/views.py` file for views, and `index/urls.py` for URLs. `index/templates/index` holds HTML / CSS / JS.


- Account
    
    The Account app currently handles authentication, together with the Django auth app.
  

- ShipShop
    
    The ShipShop app will handle the ship catalogue, ship entry adding / editing / removing, ship searching, etc...

.
