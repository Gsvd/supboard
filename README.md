# SupBoard
*last edit on 2018-01-19*

#### description

SupBoard is a tool developed and maintained by Guillaume Sivade for the SUPINFO Nice campus.

#### installation

* install python 3 and pip
* go to the root app folder
* ``` pip install -r requirements.txt ```
* ``` python manage.py makemigrations ```
* ``` python manage.py migrate ```
* ``` python manage.py createsuperuser ``` *this will be the app admin*
* ``` python manage.py runserver 0.0.0.0:{port} --insecure ``` *port is optional, insecure is to get files statically, this mode is not recommended, read [the official documentation before](https://docs.djangoproject.com/en/1.11/howto/static-files/)*
* go to ``` ip:{port} ```

![preview](https://i.imgur.com/Q22q2HV.png)
