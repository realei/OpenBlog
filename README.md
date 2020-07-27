# OpenBlog

This is an Open Source Blog based on Wagtail CMS, Bulma, and Vue.js

## Google Kubernetes Engine Configuration 

This project is currently runs on [Google Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine) 
The swagger api document is available at url: http://www.realei.tech/swagger/
### Install Cloud SQL Proxy(PostgreSQL)
1. [Installing the Cloud SQL Proxy](https://cloud.google.com/python/django/kubernetes-engine#installingthecloudsqlproxy)
2. [Creating a Cloud SQL Instance(PostgreSQL)](https://cloud.google.com/python/django/kubernetes-engine#creating_a_cloud_sql_instance)
3. [Initializing your Cloud SQL instance](https://cloud.google.com/python/django/kubernetes-engine#initializing_your_cloud_sql_instance)
4. [Creating a service account](https://cloud.google.com/python/django/kubernetes-engine#creating_a_service_account)
5. [Configing the database settings](https://cloud.google.com/python/django/kubernetes-engine#configuring_the_database_settings)

### Deploying OpenBlog to Googke Kubernetes Engine(GKE), GCS_BUCKET and Cloud SQL
1. [Setting ur your GKE configuration](https://cloud.google.com/python/django/kubernetes-engine#setting_up_your_configuration_)
2. [Collect and upload static and media resources](https://cloud.google.com/python/django/kubernetes-engine#collect_and_upload_static_resources)
'''
gsutil mb gs://[YOUR_GCS_BUCKET]
gsutil defacl set public-read gs://[YOUR_GCS_BUCKET]

'''
'''
gsutil -m rsync -r ./static gs://[YOUR_GCS_BUCKET]/static
gsutil -m rsync -r ./media gs://[YOUR_GCS_BUCKET]/media
'''




[How to config kubernetes with Cloud SQL](https://cloud.google.com/sql/docs/postgres/connect-kubernetes-engine)



## Run debug mode without docker 
1. How to configure 

2. export env files to the ENV by:
   "set -a; source ./.env.dev; set +a"
3. if you have a local virtual env, for example "openlog-env", you can:
   "echo 'set -a; source ./.env.dev; set +a' >> ./openblog-env/bin/postactivate"
Details about python evironment variables for web app, please click [here](https://help.pythonanywhere.com/pages/environment-variables-for-web-apps) 
## Run OpenBlog with docker-compose

1. docker-compose up -d --build
2. to create a super user, you can use: 
   docker exec -it container_id python manage.py createsuperuser


