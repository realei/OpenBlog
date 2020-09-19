# eAspis

"Aspis" is an ancient Greek which means shield. The eAspis is an opensource project which protect personal privacy on the internet, expecially for personal photos and videos

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
3. [Setup Google Kubernetes Engine(GKE)](https://cloud.google.com/python/django/kubernetes-engine#set_up_gke)
4. [Setup Cloud SQL](https://cloud.google.com/python/django/kubernetes-engine#set_up_cloud_sql)
5. [Deploy OpenBlog to GKE](https://cloud.google.com/python/django/kubernetes-engine#deploy_the_app_to_gke)
6. Generate Base64 encoded password for secret
7. Update files upder *./manifest*
8. Run the kubectl command to deploy the cluster and expose the service

   ` kubectl apply -f manifest/.`

9. Get the External Ip from GKE(where your OpenBlog service is exposed)

   `kubectl get services -n openblog
   NAME               TYPE           CLUSTER-IP   EXTERNAL-IP      PORT(S)        AGE
   openblog-service   LoadBalancer   10.0.7.7     35.XXX.XXX.XXX   80:32488/TCP   2d22h`

Reference: *[How to config kubernetes with Cloud SQL](https://cloud.google.com/sql/docs/postgres/connect-kubernetes-engine)*


## Run OpenBlog with docker-compose
1. Update Django env setting files via '.env.dev' and '.env.dev.db'
1. 'docker-compose up -d --build'
2. to create a super user, you can use: 

   `docker exec -it container_id python manage.py createsuperuser`


## Run debug mode without docker 
1. Update Django env setting files via '.env.dev' and '.env.dev.db' 
2. Export env files to the ENV by:

   `set -a; source ./.env.dev; set +a`

3. if you have a local virtual env, for example `openlog-env`, you can:

   `echo 'set -a; source ./.env.dev; set +a' >> ./openblog-env/bin/postactivate`

Details about python evironment variables for web app, please click [here](https://help.pythonanywhere.com/pages/environment-variables-for-web-apps) 
