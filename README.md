## Local development

To run this project in your development machine, follow these steps:

1. (optional) Create and activate a [virtualenv](https://virtualenv.pypa.io/) (you may want to use [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/)).


2. Fork this repo and clone your fork:

    `git clone git@github.com:Modiao/ayomi_modou.git`

3. Install dependencies:

    `pip install -r requirements.txt`

4. Create a development database:

    `./manage.py migrate`

5. Create a development database:

    `./manage.py createsuperuser`

6. If everything is alright, you should be able to start the Django development server:

    `./manage.py runserver`

6. Open your browser and go to http://127.0.0.1:8000, you will be greeted with a welcome page.


## Local development using Docker

1. Create a .env file

2. Set the variables :DB_HOST, DB_NAME, DB_USER, DB_PASS

3. Add the address: `0.0.0.0` on ALLOWED_HOSTS (settings.py)

4. run  [docker-compose up --build] to start the project using docker



