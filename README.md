# crm_api

Customer Relational Management with django rest framework

# Create virtual environment

```
python -m venv venv
```

# Activate virtual environment

```
.\venv\Scripts\Activate.ps1

python.exe -m pip install --upgrade pip
```

# Install packages

# Add to requirements file

```
django
djangorestframework
pyyaml
requests
django-cors-headers
```

# Run the command

```
pip install -r requirements.txt
```

# Setting project

```

django-admin startproject core .

python manager.py startapp api

```

# Run the project

```
python manage.py runserver 8000
```

# Create api

```
python manage.py startapp api
```

# Create model and make migration

```
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Statu(models.Model):
    description = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    updated = models.DateTimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.description
```

```
python manage.py makemigrations
python manage.py migrate
```

# Test the model

```
python manage.py shell

from models import Status

```

# Create user

```
python manage.py createsuperuser --username=admin --email=ramses2099@gmail.com

```

## Add djangorestframework-simplejwt authentication

```
pip install djangorestframework-simplejwt
```

## Add to settings configuration

```
REST_FRAMEWORK = {
    # JWT Authentication
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
    'DEFAULT_AUTHENTICATION_CLASSES': (
        ...
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
    ...
}
```
