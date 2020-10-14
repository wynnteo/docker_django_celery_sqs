from celery import task
from .models import Product 
from rest_framework.generics import get_object_or_404
import time

def run_job(product_id):
	update_field.delay(product_id)

@task(name="update_field", acks_late=True, autoretry_for=(InstanceTerminatingError,), reject_on_worker_lost=True)
def update_field(product_id):
	print("Start update_field: %s, %s" % product_id, time.ctime())
	time.sleep(20)
	job = get_object_or_404(Job.objects.all(), pk=product_id)
	job.status = 'Success'
	job.save()
	print("End update_field: %s" % time.ctime())
