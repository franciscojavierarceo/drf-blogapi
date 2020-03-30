# Django Rest Framework Blog API + React Native 

## DRF + Docker

Make sure you have Docker installed.

To build this the first time you simply have to run: 
```
$ git clone git@github.com:franciscojavierarceo/drf-blogapi.git
$ cd drf-blogapi
$ docker-compose build .
```

To generate the three .env files (.env, qa.env, uat.env) simply run: 
```
$ echo "ENVIRONMENT=development" > .env
$ echo "ENVIRONMENT=quality-assurance" > qa.env
$ echo "ENVIRONMENT=user-acceptance-testing" > uat.env
$ echo "SECRET_KEY=uj123412sad@$^@)#f&&#nylxh9s2$rtgp!a4wsnyh" | tee -a .env qa.env uat.env
$ echo "DEBUG=1" | tee -a .env qa.env 
$ echo "DEBUG=0" >> uat.env
$ echo "EMAIL_HOST_PASSWORD=None" | tee -a .env qa.env uat.env
$ echo "DB_NAME=postgres" | tee -a .env qa.env uat.env
$ echo "DB_USER=postgres" | tee -a .env qa.env uat.env
$ echo "DB_PASSWORD=postgres" | tee -a .env qa.env uat.env
$ echo "DB_HOST=db" | tee -a .env qa.env uat.env
$ echo "DB_PORT=5432" | tee -a .env qa.env uat.env

$ docker-compose run web bash build.sh 
$ docker-compose down
$ docker-compose up --build
```

You should now be able to see the homepage on https://localhost:8000


Note that this creates a default user with the following details:
- username: admin
- email: admin@djangox.com
- password: password123


Then to rebuild the project you have to run:
```
$ docker volume rm drf-blogapi_postgres_data    # this wipes the postgres database created by docker
$ docker-compose run web bash build.sh          # this runs the migrations and creates the admin user
$ docker-compose down                           # just to stop the service to relaunch
$ docker-compose up --build
$ docker-compose exec web python manage.py collectstatic
$ docker-compose -f docker-compose-uat.yml up --build
```

To test the DRF registration and login endpoints go to a separate terminal and try:

```
# This was valid for the old username
# curl -X POST -d "username=testuser2&email=testuser2@djangox.com&password1=random0232&password2=random0232" http://localhost:8000/api/v1/rest-auth/registration/
# curl -X POST -d "username=testuser2&password=random0232" http://localhost:8000/api/v1/rest-auth/login/

# with the custom username try:
curl -X POST -d "email=testuser3@djangox.com&password1=random0232&password2=random0232" http://localhost:8000/api/v1/rest-auth/registration/
curl -X POST -d "email=testuser3@djangox.com&password=random0232" http://localhost:8000/api/v1/rest-auth/login/
```

## React Native + Yarn

Make sure you've installed [expo](https://expo.io/tools#cli), [node.js](https://nodejs.org/en/), and the [Expo Client App](https://expo.io/tools#client) from the App store.

```
$ cd drf-expo-demo
$ npm install
$ npm start
```

Scan the QR code using your camera on your phone and it should take you to a working version of the app.
