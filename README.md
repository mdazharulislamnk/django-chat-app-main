Django Chat App
===============

A simple room-based chat app built with Django and jQuery polling. 
Users enter a room name and username, then chat with messages stored in SQLite.

------------------------------------------------------------
Features
------------------------------------------------------------
- Create or join rooms by name.
- Inline CSS templates for zero static setup.
- AJAX endpoints to send and fetch messages.
- SQLite models: Room and Message.

------------------------------------------------------------
Project Layout
------------------------------------------------------------
django-chat-app-main/
├─ manage.py
├─ db.sqlite3
├─ djangochat/
│  ├─ __init__.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ asgi.py
│  └─ wsgi.py
├─ chat/
│  ├─ __init__.py
│  ├─ apps.py
│  ├─ admin.py
│  ├─ models.py
│  ├─ views.py
│  ├─ urls.py
│  └─ tests.py
└─ templates/
   ├─ home.html
   └─ room.html

------------------------------------------------------------
Quick Start
------------------------------------------------------------
1. Install Django
   pip install django

2. Configure Secret Key
   Generate a key:
   python -c "from django.core.management.utils import get_random_secret_key as g; print(g())"
   Paste it into djangochat/settings.py:
   SECRET_KEY = 'paste-generated-key'

3. Initialize the Database
   python manage.py makemigrations chat
   python manage.py migrate

4. Run the Server
   python manage.py runserver 127.0.0.1:8080
   Open: http://127.0.0.1:8080/
   Use another free port if needed.

------------------------------------------------------------
Routes
------------------------------------------------------------
Method   URL                        Description
GET      /                          Home form (room_name, username)
POST     /checkview                 Create/get room, redirect to /room/<name>/?username=<user>
GET      /room/<name>/              Room page with messages
GET      /getMessages/<room>/       JSON list of messages for polling
POST     /send                      Create a message (room_id, username, message)

------------------------------------------------------------
Username Propagation
------------------------------------------------------------
- checkview appends ?username=<user> to the room URL.
- room view reads that value and injects it into the template’s hidden field.
- send view saves Message.author from the posted username.

------------------------------------------------------------
What’s Used and Why
------------------------------------------------------------
Technology        Purpose
------------------------------------------------------------
Python + Django   URL routing, ORM, migrations, admin, template rendering
SQLite            Default dev DB; zero config, db.sqlite3 auto-created
Templates + CSS   Avoids static setup; quick start
jQuery (CDN)      Polling + AJAX form submit

------------------------------------------------------------
App Modules
------------------------------------------------------------
djangochat/settings.py
- SECRET_KEY (generated)
- INSTALLED_APPS includes 'chat'
- DATABASES uses SQLite
- Templates path configured

djangochat/urls.py
- Root URLConf delegating to app URLs and admin

chat/models.py
- Room(name unique)
- Message(room FK, author, content, created_at)

chat/urls.py
- '', room/<str:name>/, checkview, getMessages/<str:room>/, send

chat/views.py
- home, checkview, room, get_messages, send

templates/home.html
- Form to enter room_name and username; posts to /checkview; inline CSS

templates/room.html
- Renders messages
- Hidden inputs for username and room_id
- jQuery polls /getMessages and POSTs to /send

------------------------------------------------------------
Windows Scaffolding (Optional)
------------------------------------------------------------
mkdir django-chat-app-main && cd django-chat-app-main
mkdir djangochat chat templates
type NUL > manage.py
cd djangochat && (type NUL > __init__.py) && (type NUL > settings.py) && (type NUL > urls.py) && (type NUL > asgi.py) && (type NUL > wsgi.py) && cd ..
cd chat && (type NUL > __init__.py) && (type NUL > apps.py) && (type NUL > admin.py) && (type NUL > models.py) && (type NUL > views.py) && (type NUL > urls.py) && (type NUL > tests.py) && cd ..
cd templates && (type NUL > home.html) && (type NUL > room.html) && cd ..

SQLite file is created automatically during migrate.

------------------------------------------------------------
Tips and Pitfalls
------------------------------------------------------------
- If you see “Unknown command,” retype without hidden characters.
- If you see “no such table: chat_room,” run:
  python manage.py makemigrations chat
  python manage.py migrate
- To use admin:
  python manage.py createsuperuser
  Visit /admin
