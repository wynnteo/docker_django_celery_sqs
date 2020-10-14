import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "docker_django_tutorial.settings")

# create a celery instance
app = Celery("docker_django_tutorial")
# load the celery configuration
app.config_from_object("django.conf:settings", namespace="CELERY")
# look for celery task
app.autodiscover_tasks()

# simple task to print all the metadata
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))