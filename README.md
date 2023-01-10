# RP-Taxi API Services

transportation company with an app that allows passengers to hail a ride and drivers to charge fares and get paid.

<br>

## launch
```
docker-compose up -d --build
docker-compose exec app python manage.py makemigrations 
docker-compose exec app python manage.py migrate
docker-compose exec app python manage.py collectstatic
docker-compose exec app python manage.py createsuperuser
```
<br><hr>


Build code with docker compose
```
docker-compose build
```

Run the built container
```
docker-compose up -d
```



Build the image and spin up the containers:
```
docker-compose up -d --build
```



Migrate databases
```
docker-compose exec app python manage.py makemigrations
docker-compose exec app python manage.py migrate
```




Collect static files
```
docker-compose exec app python manage.py collectstatic
```



Create super user
```
docker-compose exec app python manage.py createsuperuser
```
