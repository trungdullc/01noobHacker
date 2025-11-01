# django
```
Description: python framework

Documentation: https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django/Introduction
Download: https://www.djangoproject.com/
Install:                                                // homebrew is mac package manager
    Python3         // sudo apt install python3-pip     // brew install python3
    pipenv          // sudo apt install pipenv          // pip3 install pipenv

Resources:
    https://www.w3schools.com/django/index.php
    https://ia600604.us.archive.org/3/items/ebooks_202307/djangoforbeginners.pdf
```

### New django project
```python
$ mkdir -p project/django
$ cd project/django

# Optional: create a virtual environment first (recommended)
$ python -m venv myenv                                                          pipenv install django==2.1
# Activate virtual environment
$ source myenv/bin/activate         # myenv\Scripts\activate (for Windows)      pipenv shell

# Install Django
(myenv) pip install django
# Check if installed
(myenv) django-admin --version

# Create new Django project here
(myenv) django-admin startproject newProject1 . ❤️❤️❤️❤️❤️

# Run the development server
(myenv) python manage.py runserver ❤️❤️❤️❤️❤️

# Deactivate virutal environment
(myenv) deactivate
```

### Create new app
```python
# Note: Each app is basically a SPA (auth, payment, about, hello)
(myenv) python manage.py startapp hello

# Open VSC
(myenv) code .
# Open settings.py and look at INSTALLED_APPS
   add 'hello',
```

### Setup view
```python
# view is what show to user when go to url
# Open hello > views.py
from django.http import HttpResponse    # get HttpResponse() from http module/subfolder from django package/folder

def myView(request):
    return HttpResponse("Hello Hackers")
```

### Fix urlpatterns to link correctly
```python
from hello.views import myView          # get myView() from views.py from hello package/folder

# urls.py and urlpatterns
   path("sayHi", myView)
```

## Back to README.md
[BACK](../README.md)