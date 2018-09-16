# HOWTO

## Configure

### BD
```$ python manage.py makemigrations```
```$ python manage.py migrate``` 

### RootUser
```$ python manage.py shell```
```
	>>> from django.contrib.auth.models import User
	>>> user=User.objects.create_user('ifsp', password='ifsp')
	>>> user.is_superuser=True
	>>> user.is_staff=True
	>>> user.save()
	>>> exit()
```

## Run  
```python manage.py runserver 80```

## Auth
```
curl -X GET \
  http://127.0.0.1/api/auth/ \
  -H 'authorization: Basic aWZzcDppZnNw' \
  -H 'cache-control: no-cache'
```