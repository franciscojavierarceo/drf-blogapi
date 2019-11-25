# Django Rest Framework Blog API + React Native 

## DRF + Docker

Make sure you have Docker installed and then run the following: 

```
$ git clone git@github.com:franciscojavierarceo/drf-blogapi.git
$ cd drf-blogapi
$ docker volume rm drf-blogapi_postgres_data
$ docker-compose run web bash build.sh 
$ docker-compose down
$ docker-compose up --build
```

To test the DRF registration and login endpoitns go to a separate terminal and try:

```
curl -X POST -d "username=testuser2&email=testuser2@djangox.com&password1=random0232&password2=random0232" http://localhost:8000/api/v1/rest-auth/registration/
curl -X POST -d "username=testuser2&password=random0232" http://localhost:8000/api/v1/rest-auth/login/
```

## React Native + Yarn

Make sure you've installed [expo](https://expo.io/tools#cli), [node.js](https://nodejs.org/en/), and the [Expo Client App](https://expo.io/tools#client) from the App store.

```
$ cd drf-expo-demo
$ npm install
$ npm start
```

Scan the QR code using your camera on your phone and it should take you to a working version of the app.
