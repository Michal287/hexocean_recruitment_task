SETUP HEXOCEAN PROJECT

<h3>_Clone repository_</h3>
```
git clone xxx
```
<h3>_Go to the folder_</h3>
```
cd hexocean
```
<h3>_Then build and run Docker_</h3>
```
docker-compose up
```
<h3>Congratulations! Your server is already running at http://127.0.0.1:8000</h3>

Your superuser has been already created automatically. 
```
Login: admin
Password: admin
```

Also I added the 3 tiers that were included in task with their specifications
```
    - Basic
    - Premium
    - Enterpise
```   
Always you can go to create new user or custom tier in admin panel :)

<h1>Endpoints</h1>

<h3>_Get list of images_</h3>
```
GET: http://127.0.0.1:8000/api/image/
```


<h3>_Upload image_</h3>
```
POST: http://127.0.0.1:8000/api/image/
```


<h3>_Create binary image link_</h3>
```
POST: http://127.0.0.1:8000/api/image/<image_id>/binary-image/
```


<h3>_Get binary image link_</h3>
```
GET: http://127.0.0.1:8000/api/image/<binary_image_link>/
```






