# Silvertec Rest API Challenge - Frontend

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 8.3.19.

## Install and run

### Using Dockerfile and docker-compose

First you need to init a daemon with dockerd, so run dockerd:

    root $ dockerd

OR

    root $ sudo dockerd

Now, clone this repository at a root directory and after this, access the silvertec/frontend directory:

    root $ cd silvertec/frontend

And then with Docker and docker-compose, run:

    root/silvertec/frontend $ docker-compose up --build

This command above will run the server automatically with `ng serve` command. Navigate to `http://localhost:4200/` to take a look at frontend part of Silvertec Rest API Challenge. 

The single page application will consume the Silvertec Rest API at https://silvertec.herokuapp.com/ so, due to Heroku free applications characteristics, wait a little bit to wake up the Heroku Dyno. 

### Using local Angular environment

Proceed to `root/silvertec/frontend` and run:

     root/silvertec/frontend $ npm install @angular/cli
     root/silvertec/frontend $ ng serve

Now you'll see the Angular SPA consuming Silvertec Rest API.

### Deployed Frontend

You too can take a look at Angular single page application consuming the Silvertec Rest API at Heroku deployed app:

#### https://angularsilvertec.herokuapp.com

