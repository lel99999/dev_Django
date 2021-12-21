# dev_Django
Django RESTful Standalone and Web Service Development

##### Check uf django is installed and which version
```
$python -m django --version
```

or 
```
$python -c "import django;print(django.get_version());"
```

##### Create Project
```
$django-admin startproject devSite

## Project Structure

devSite/
    manage.py
    devSite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

##### Django Admin Info
- [https://docs.djangoproject.com/en/4.0/ref/django-admin/](https://docs.djangoproject.com/en/4.0/ref/django-admin/) <br/>


##### Error Notes
- django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty

  django setttings notes: <br/>
  - [https://docs.djangoproject.com/en/4.0/topics/settings/](https://docs.djangoproject.com/en/4.0/topics/settings/) <br/>
  - [https://docs.djangoproject.com/en/4.0/ref/settings/](https://docs.djangoproject.com/en/4.0/ref/settings/) <br/>

  ```
  export DJANGO_SETTINGS_MODULE=myproject.settings
  django-admin runserver
  ```
