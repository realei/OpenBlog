# OpenBlog
This is an Open Source Blog based on Wagtail CMS, Bulma, and Vue.js

## Run debug mode without docker 
1. export env files to the ENV by:
   "set -a; source ./.env.dev; set +a"
2. if you have a local virtual env, for example "openlog-env", you can:
   "echo 'set -a; source ./.env.dev; set +a' >> ./openblog-env/bin/postactivate"
refer:
https://help.pythonanywhere.com/pages/environment-variables-for-web-apps/
## Run OpenBlog with docker-compose

1. docker-compose up -d --build
2. to create a super user, you can use: 
   docker exec -it container_id python manage.py createsuperuser

## Google Kubernetes Engine Configuration 

1. [How to config kubernetes with Cloud SQL](https://cloud.google.com/sql/docs/postgres/connect-kubernetes-engine)

## As a contributer:
1. code check:
'''
flake8 --ignore=E501,F401 .
'''
