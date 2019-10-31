## Developer Guide

#### create VM(Optional)

##### Check Python Version
>python --version

##### Create new virtual environment
>python -m venv lynxenv

##### Activate the virtual environment
###### Linux, MAC
>source lynxenv/bin/activate

or

>. lynxenv/bin/activate

###### Windows
>.\lynxenv\Scripts\activate.bat

##### Confirm python env and verion
>(lynenv)$python --version

>Python 3.7.2

##### Deactivate the virtual environment
>(lynxenv)$deactivate

##### Install packages
>(lynenv)$pip install [package anme]

If you facing kinds of below issues, try to use ```pip install [package anme] --user```

>ERROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied:'c:\\program files\\python37-32\\Lib\\site-packag.py'

>Consider using the `--user` option or check the permissions.


#### create project
```python manage.py startproject yourproject```

#### create new app
```python manage.py startapp yournewapp```

#### install libraries
```pip install -r requirements.txt```


#### table update

1. save table update
```python manage.py makemigrations ```

2. apply table update
``` python manage.py migrate ```

if you create a new table then, add below code to ```yournewapp/admin.py``` to apply the changes to admin

```from .models import yournewmodel ```

```admin.site.register(yournewmodel)```

#### superuser management
```python manage.py createsuperuser```

#### run server
```python manage.py runserver```

#### Create requirements.txt
```pip freeze > requirements.txt```

#### .gitignore
```git rm -r --cached .```

#### Djangoの設定ファイル（settings）を切り替える
```gunicorn --env DJANGO_SETTINGS_MODULE=myproject.settings.production myproject.wsgi```
