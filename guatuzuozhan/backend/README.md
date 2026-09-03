# guatuzuozhan backend

Django REST Framework backend using the existing `guatuzuozhanv2` database. Copy `.env.example` to `.env`, install `requirements.txt`, and run `py manage.py runserver 127.0.0.1:8000`.

`users` and `departments` are mapped with `managed = False`. Do not run migrations until the existing schema has been reviewed.
