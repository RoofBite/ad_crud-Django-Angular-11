# ad_crud

Run with docker:

docker-compose build

docker run -p 8000:8000 ad-crud

Go to: http://localhost:8000/



Admin panel: http://localhost:8000/admin

    login: admin
    password: admin


Api endpoints:

    'GET, POST' : '/api/offer'
    'GET, POST' : '/api/category'
    'GET, PUT, DELETE' : 'api/offer/{id}'
    'PUT, DELETE' : 'api/offer/{id}'



IF YOU WANT:

Value of variable secret_key in settings.py is stored in enviroment variable, it can be set before starting the project.
