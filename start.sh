#!/bin/bash
#sleep 999999
pipenv run ./manage.py collectstatic --noinput
pipenv run ./manage.py migrate --noinput
cd frontend
NODE_ENV=development PORT=3001 HOST=0.0.0.0 API_MOCK=1 npm run dev &
NODE_ENV=development PORT=3000 HOST=0.0.0.0 API_MOCK=0 npm run dev &
cd ..
pipenv run ./manage.py runserver 0.0.0.0:8000
