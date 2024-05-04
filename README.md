# World-of-Games-1312

v2.0.5
![Banner GIF](static/images/wog-banner.gif)
## This is a collection of mini-Python games, made to be loads of fun! 
Jump right in and enjoy all the different games waiting for you in the World of Games!

## The Guess Game
The Guess Game starts by randomly picking a secret number between 0 and the "difficulty." Then, you have to guess what that secret number is by typing in your guess!

## The Currency Roulette Game
Currency Roulette Game! It uses special magic to find out how much one U.S. dollar is worth in Israeli Shekels (ILS). Then, it picks a secret number between 1 and 100, and you have to guess how much that is in U.S. dollars converted to Israeli Shekels! How close you get depends on how hard you want the game to be!

## The Memory Game
The Memory Game is all about testing your memory! First, it shows you a bunch of random numbers quickly—whoosh! Then, it's your turn to try to remember what those numbers were and type them! Can you remember them all? Let's find out!

---

This project is a web app version of World of Games.

## Pull Latest Docker Version
```
docker run -d -p 8777:8777 -v $(pwd):/app/database gil9192/world-of-games1312:latest
```

## Local Setup

To setup the environment.

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Provide External DB Credentials
The ".env" file contains different environment variables.
In order to use with external database "APP_DB" should be changed from "local" to "remote".
Please make sure to define the DB password and connection parameters if using remote database.
https://docs.djangoproject.com/en/4.2/ref/settings/#databases

## Local Run
To build and run locally.

```
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8777
```

## To build and run as Docker Container

```
docker-compose build
docker-compose up -d
```
