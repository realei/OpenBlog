# OpenBlog
This is an Open Source Blog based on Wagtail CMS, Bulma, and Vue.js

## Run OpenBlog with docker-compose

1. docker-compose up -d --build
2. to create a super user, you can use: 
   docker exec -it container_id python manage.py createsuperuser
