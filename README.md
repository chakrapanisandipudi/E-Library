# Django CRUD Example Apps

This is a small Django project to demonstrate Django E-Library functionality, it
consist of  small applications:


## Install Required Packages

The Django CRUD project only need a single Python package "Django", it was built and
tested with Django 2.x version. To install it use the following command:

    pip install -r requirements.txt


## Running the Application

Before running the application we need to create the needed DB tables:

    ./manage.py migrate

Now you can run the development web server:

    ./manage.py runserver

To access the applications go to the URL <http://localhost:8000/>


## I need a user and password to access "books\student_register"

Yes, the "books\student_register" demonstrate how Login can work with Django users, and you do
need to create a user to test it, you can create a user using the following command:

    ./manage.py createsuperuser

To create a normal user (non super user), you must login to the admin page and
create it: <http://localhost:8000/admin/>
