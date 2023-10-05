# api.subito.message.house-network  <img src="https://user-images.githubusercontent.com/45575898/184987964-64477382-1df1-4512-9b77-9d6ec0eef470.jpg" width="60" height="60" />

middleware-engine used as relation with dbe for real-estate on subito.it

clone repository and move in:
```
$ git clone https://github.com/lucaimbalzano/api.subito.message.house-network
$ cd api.subito.message.house-network
```

create virtual environment
```
$ python3 -m venv env

windows:
$ .\env\Scripts\activate 
linux:
$source ./env/bin/activate
or 

(if you haven't pipenv)

$ pipenv --python 3.10 install --dev
then:
$ pipenv shell
```


install all dependencies:

```
$ pip install wheel
$ pip install -r requirements.txt
```

runserver
```
$ python3 manage.py runserver
```

create a new super user for admin: http://127.0.0.1:8000/admin
```
$ python3 manage.py createsuperuser
current username: lucai
current password: password
```


inizialization

```
$ pip3 install -U django djangorestframework django-filter drf-yasg

NOTE: The commands above include drf-yasg for auto-generated Swagger documentation and django-filter for filtering on endpoints. Feel free to remove those if not needed

```

install django rest fw

```
# pip3 install django djangorestframework
```

add mondule django

```
$ django-admin startapp api

```

make a file to edit db

```
to get init DB use
$ python3 manage.py makemigrations api
$ python3 manage.py migrate 

to apply all db structure use
$ python3 manage.py migrate

```

local pswd pgAdmin
postgres



Docker:
```
$  docker build --no-cache -t web .
$ docker-compose --env-file .env up


$ docker build --no-cache -t web -f ./docker/images/app/Dockerfile .

give first permission to our volume db data
$ sudo chmod -R 777 ./docker/sql/
$ sudo chmod -R 777 ./postgresdb/data
$ docker build --no-cache -t house-net-api.postgres -f ./docker/images/postgres/Dockerfile .

env UID=${UID} GID=${GID} docker-compose -f ./docker/docker-compose.yml --env-file .env up
$ docker-compose -f ./docker/docker-compose.yml --env-file .env up
```







last:
https://stackoverflow.com/questions/70091829/backend-docker-image-does-not-wait-until-db-becomes-available




ᵈᵉᵛᵉˡᵒᵖᵉᵈ ᵇʸ 𝙡𝙪𝙘𝙖𝙞𝙢𝙗𝙖𝙡𝙯𝙖𝙣𝙤@𝙜𝙢𝙖𝙞𝙡.𝙘𝙤𝙢