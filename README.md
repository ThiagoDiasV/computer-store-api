# Silvertec Rest API Challenge

## Install and run

### With Dockerfile and docker-compose

With this repository in your machine, access the silvertec directory:
    
    $ cd silvertec

And then with Docker and docker-compose, do:

    $ docker-compose up --build

This command above will: 
- Create and migrate database 
- Ask you to create a superuser
- Run unit tests
- Run server

Now you will be able to navigate through the Silvertec API.

### With Python 3.7

Like above, prefer to create a Python virtual environment and inside silvertec directory:

    python manage.py migrate
    python manage.py runserver


## Run the tests

During development some unittests were made. You can cover your Silvertec API with these tests running:

    python manage.py test

# Rest API

The Rest API is described below

## Endpoints

    /api/processors/
    /api/motherboards/
    /api/memories/
    /api/graphiccards/
    /api/computers/
    /api/orders/
    /api/users/

## API documentation endpoints

`In these endpoints it's possible to user two another UI's to interate with Silvertec API`

    /openapi/swagger/
    /openapi/redoc/
