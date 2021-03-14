# exercise_tracker

An exercise tracker app where users can track their exercise routines on their calendar. 
## <a href="https://harikaduyu-exercise-tracker.herokuapp.com/">Demo</a>

## Configuring the app
I used Digital Ocean Spaces to store my staticfiles which is very similar to AWS S3. So my configuration is like the following: 

```
EX_TRACKER_ENV = 'develop-or-prod'
SECRET_KEY = 'your-django-secret-key'
DATABASE_URL = 'postgres://<user>:<password>@<host>:<port>/<database>'
AWS_ACCESS_KEY_ID = 'digital-ocean-access-key-id'
AWS_SECRET_ACCESS_KEY = 'digital-ocean-secret-access-key'
AWS_STORAGE_BUCKET_NAME = 'digital-ocean-space-name'
AWS_S3_REGION_NAME = 'region-name-of-your-space-for-example-fra1'
AWS_S3_ENDPOINT_URL = 'https://${AWS_S3_REGION_NAME}.digitaloceanspaces.com'
```

## Running app locally using docker
You can easily run it on your local machine after cloning the repo. 
Add a folder named env in your root. Add "djnago.env" file inside this folder with the variables described above. 
And run the following comments.
```console
docker-compose build
docker-compose up
```

## Running app locally without docker
If you are not familiar with docker, just set your environment variables to your environment. 
Make sure you have pipenv. If not then install it by running:

```console
pip install pipenv
```

Then go to the project folder and run

```console
pipenv install
```
This will download all the necessary packages defined in Pipfile and Pipfile.lock

Afterwards you can run 

```console
pipenv shell
```
and you are inside the virtual env with all the required packages. 

Finally;
```console
python manage.py runserver
```
And your app is running!
