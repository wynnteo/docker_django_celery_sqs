#Use the Python3.7.2 container image
FROM python:3.7.2-stretch

#Copy the current directory contents into the container.
COPY . /usr/src/app   

#Set the working directory to /usr/src/app
WORKDIR /usr/src/app

#Install the dependencies
RUN pip install -r requirements.txt

RUN python manage.py collectstatic --noinput

#Run the command to start server
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#CMD ["uwsgi", "--http", "0.0.0.0:8000", "--module", "docker_django_tutorial.wsgi"]
