# Silvertec Rest API Challenge - Backend

## Install and run

### Using Dockerfile and docker-compose

First you need to init a daemon with dockerd, so run dockerd:

    root $ dockerd

OR

    root $ sudo dockerd

Now, clone this repository at a root directory and after this, access the silvertec/backend directory:
    
    root $ cd silvertec/backend

And then with Docker and docker-compose, run:

    root/silvertec/backend $ docker-compose up --build

This command above will: 
- Create and migrate database 
- Run unit tests
- Run server

Now you will be able to navigate through the Silvertec API.
To have authenticated user permissions, please open other terminal instance at root container directory and create a super user using python manage.py inside the container:

    root/silvertec/backend $ docker exec -it silvertec python manage.py createsuperuser

After this, to stop the created container:

    root/silvertec/backend $ docker-compose down

### Using local Python 3.7

Prefer to create a Python virtual environment and then

    (venv) root $ cd silvertec/backend

    (venv) root/silvertec/backend $  pip install -r requirements.txt

After installing requirements run:

    (venv) root/silvertec/backend $ python manage.py migrate
    (venv) root/silvertec/backend $ python manage.py runserver

Obs: if you already tested running server using Docker and docker-compose, please delete sqlite database generated locally by docker-compose to migrate database correctly using local Python. 

### Deployed API

You can use Silvertec Rest API at Heroku deployed app:

#### https://silvertec.herokuapp.com/

## Run the tests

You can cover Silvertec API with unit tests running:

### Using Docker

    root/silvertec/backend $ docker exec -it silvertec python manage.py test api.tests

### Using Python 3.7 

    (venv) root/silvertec $ python manage.py test

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

#### Observation about endpoints
Only authenticated users can create, update and delete processors, motherboads, memories and graphic cards.

## Examples

### List Processors
Returns json or html data with all processors in database.

- URL
    
    /api/processors/

- Method

    `GET`

- URL Params
    
    None

- Data Params
    
    None

- Success Response:

    - HTTP status code
    
        `200 OK`

    - Content 
    
        `[{"id":1,"processor_description":"Intel Core i5","processor_brand":"Intel"},{"id":2,"processor_description":"Intel   Core i7","processor_brand":"Intel"},{"id":3,"processor_description":"AMD Ryzen 7","processor_brand":"AMD"},{"id":4,"processor_description":"AMD Athlon","processor_brand":"AMD"}]`

### Create New Graphic Card
Returns json or html data with created graphic card.

- URL
    
    /api/graphiccards/

- Method

    `POST`

- URL Params
    
    None

- Data Params
    
    Required:

    `graphic_card_description=[string]`
    
    Obs: Needs authentication credentials

- Success Response:

    - HTTP status code
    
        `201 CREATED`

    - Content 
    
        `{
            "graphic_card_description": "Radeon RX 580 8GB",
            "id": 4
        }`

- Error Response

    - HTTP status code
    
        `400 BAD REQUEST`

    - Content 
    
        `{
            "graphic_card_description": [
                "\"Radeon RX 580\" is not a valid choice."
            ]
        }`

### Update Memory
Returns json or html data with updated memory card.

- URL
    
    /api/memories/:id/

- Method

    `PUT`

- URL Params
    
    Required:
    `id=[integer]`

- Data Params
    
    Required:

    `ram_description=[string]`
    `ram_size=[integer]`
    
    Obs: Needs authentication credentials

- Success Response:

    - HTTP status code
    
        `200 OK`

    - Content 
    
        `{
            "id": 1,
            "ram_description": "Hiper X",
            "ram_size": 32
        }`

- Error Response

    - HTTP status code
    
        `404 NOT FOUND`

    - Content 
    
        `{
            "detail": "Not found."
        }`

### Delete Motherboard
Returns no content.

- URL
    
    /api/motherboards/:id/

- Method

    `DELETE`

- URL Params
    
    Required:
    `id=[integer]`

- Data Params
    
    Required:

    None
    
    Obs: Needs authentication credentials

- Success Response:

    - HTTP status code
    
        `204 NO CONTENT`

    - Content 
    
        None

- Error Response

    - HTTP status code
    
        `404 NOT FOUND`

    - Content 
    
        `{
            "detail": "Not found."
        }`

## API documentation endpoints

In these endpoints it's possible to user two other UI's to interate with Silvertec API

    /openapi/swagger/
    /openapi/redoc/
