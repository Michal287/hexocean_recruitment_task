# SETUP HEXOCEAN PROJECT

#### Clone repository
```
git clone https://github.com/Michal287/hexocean
```
#### Go to the folder
```
cd hexocean
```
#### Then build and run Docker
```bash
docker-compose up
```
#### Congratulations! Your server is already running at http://127.0.0.1:8000
#### Your superuser has been already created automatically. 
```bash
Login: admin
Password: admin
```

#### Also I added the 3 tiers that were included in task with their specifications
```bash
    - Basic
    - Premium
    - Enterpise
```   
Always you can go to create new user or custom tier in admin panel :)

# Endpoints

#### Get list of images
```bash
GET: http://127.0.0.1:8000/api/image/
```


#### Upload image
```bash
POST: http://127.0.0.1:8000/api/image/
```


#### Create binary image link
```bash
POST: http://127.0.0.1:8000/api/image/<image_id>/binary-image/
```


#### Get binary image link
```bash
GET: http://127.0.0.1:8000/api/image/<binary_image_link>/
```

# How to improve projet?
* Celery to delete binary images that have expired (In the project removing are after entering the endpoint which is not optimal)






