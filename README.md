# World-of-Games-1312

This project is web app version for world of games.

## Local Setup

In order to setup the environment.

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Provide DB Credentials
The ".env" file contains different environment variables, please make sure
define DB password and connection string if needed.
https://docs.djangoproject.com/en/4.2/ref/settings/#databases

## Local Run

In order to run locally.

```
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8777
```

## Run as Docker Container

```
docker-compose build
docker-compose up -d
```
