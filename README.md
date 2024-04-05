# Project setup
I have used python Django framework.
For storing data, I have used Postgresql.
Please create a database named movierating from pgadmin.
Clone the project.
Please install python (my version 3.11.4) and/or django (my version 5.0.3) if required.
Please install missing packages if required.
From myapps/settings.py chnage the db connection parameters value from line 81 to 85 as required.
Run the following commands from terminal.
 - py manage.py makemigrations movierating
 - py manage.py migrate
 - python manage.py loaddata seed/User.json
 - python manage.py loaddata seed/Movie.json
 - python manage.py loaddata seed/Rating.json

Run the project from terminal with the following command
 - py manage.py runserver

Navigate to the route movierating/movies/ to check the application

I have solved the entire problem
