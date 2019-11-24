# Django Rest Framework Blog API


```
docker volume rm drf-blogapi_postgres_data
docker-compose run web bash build.sh 

```

To test the DRF registration and login endpoint try:

```
curl -X POST -d "username=testuser2&email=testuser2@djangox.com&password1=random0232&password2=random0232" http://localhost:8000/api/v1/rest-auth/registration/
curl -X POST -d "username=testuser2&password=random0232" http://localhost:8000/api/v1/rest-auth/login/
```

