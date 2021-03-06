# django-fundamentals

Playground for PluralSight [course] (https://www.pluralsight.com/courses/django-fundamentals)

## Starting a Django project

### create a new virtual environment using *virtualenv* 
`virtualenv -p [path\to\python.exe] django-fundamentals`

### create a new virtual enviroment using *virtualenvwrapper-win* 
`mkvirtualenv -p [path\to\python.exe] django-fundamentals`

### PyCharm can create a new virtualenv too
*File - New Project - Interpreter (Create VirtualEnv)*

## start new django project
`django-admin.py startproject [project name]`

Note: *django\bin* (where *django-admin.py* lives) must be in path.

### start new app
`python manage.py startapp [app name]`

## Model-Template-View desing pattern (vs MVC)

### Model
- Represents your data
- Each model class represents a database table

### View (*Controller* in MVC)
- Takes HTTP request and return response
- May use model to retrieve/store data
- May call a template to present data

### Template (*View* in MVC)
- Generate HTML
- Presentation logic only
