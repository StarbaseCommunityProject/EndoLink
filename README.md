# StarbaseCommunityWebsite
An open-source Starbase community website.

## How to run:

### Docker:

Docker Compose should take care of everything and automatically build the containers & run the webserver.

Run `docker-compose up` in the base directory (the folder which has the `docker-compose.yml` file).

### Not Docker:

In case you want to run the backend without Docker (not recommended), you can simply run `python manage.py runserver` in the `backend` directory. Be sure to install the necessary requirements from `backend/requirements.txt` first, though.

For the frontend, you should be able to use `ng serve` in the `frontend` directory, after the necessary steps to install Angular.

## Contact:

We primarily use [Discord](https://discord.gg/qDPF2z6Krh) for communication.

- Backend: `Max#0007`

- Frontend: `Pasu#3669`