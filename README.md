#_py_quiz HSI

|Step	|Description	                    |Command                                    |
|-------|-----------------------------------|-------------------------------------------|
|1a	    |Set up a virtual environment	    |pipenv shell                               |
|1b	    |Activate the virtual environment	|*same*, would activate automatically       |
|2a	    |Install Django	                    |pipenv install django                      |
|3	    |Set up a Django project	        |django-admin startproject <projectname>    |
|4	    |Start a Django app	                |python manage.py startapp <appname>        |
|5	    |Run project app	                |python manage.py runserver <port server>   |
|6	    |Done define models	                |python manage.py makemigrations <appname>  |
|6.1	    |Done define models	                |python manage.py migrate|
|7	    |Create super user or Admin	                |python manage.py createsuperuser|