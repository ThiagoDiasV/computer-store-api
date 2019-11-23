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

    $ python manage.py migrate
    $ python manage.py runserver


## Run the tests

You can cover Silvertec API with unit tests running:

    $ python manage.py test

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

## Examples

### List Processors
Returns json or html data with all processors in database.

- URL
    /api/processors/

- Method

    GET

- URL Params
    None

- Data Params
    None

- Success Response:

    - Code: 200 OK
    - Content: [{"id":1,"processor_description":"Intel Core i5","processor_brand":"Intel"},{"id":2,"processor_description":"Intel   Core i7","processor_brand":"Intel"},{"id":3,"processor_description":"AMD Ryzen 7","processor_brand":"AMD"},{"id":4,"processor_description":"AMD Athlon","processor_brand":"AMD"},{"id":5,"processor_description":"Intel Core i5","processor_brand":"Intel"},{"id":6,"processor_description":"Intel Core i7","processor_brand":"Intel"}]

## API documentation endpoints

In these endpoints it's possible to user two another UI's to interate with Silvertec API

    /openapi/swagger/
    /openapi/redoc/
