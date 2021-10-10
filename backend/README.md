## Current Django Apps:


- #### Account
  The Account app handles authentication using JWT.

- #### Factions
  The Factions app handles factions, faction membership, faction advertisements, etc...

- #### Index
  The Index app is deprecated and currently just holds some util routes for the API:
  - get_player_count
  - get_starbase_news
  
  This will be moved to a new app in the future.

- #### ShipShop 
  The ShipShop app handles the ship catalogue, ship entry adding / editing / removing, ship searching, etc...

- #### Settings
  The settings module is not a Django app. It holds the base settings file and derivative production and development settings files.
