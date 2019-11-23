# Silvertec Rest API Challenge

## Install and run

### With Dockerfile and docker-compose

With this repository in your machine, access the silvertec directory:
    
    $ cd silvertec

(Optional) To avoid any incovenience to your operational system, create a Python virtual environment with your preferred virtual environment generator like venv...
    
    $ python -m venv venv

...and activate it:

`On Linux and MacOS` 

    $ source venv/bin/activate

`On Windows`

    /> venv\Scripts\activate

And then with Docker and docker-compose, do:

    (venv) docker-compose up --build

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
