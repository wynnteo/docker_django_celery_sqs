from celery import shared_task
from .models import Product 
from rest_framework.generics import get_object_or_404
import time

def run_job(product_id):
	update_field.delay(product_id)

@shared_task
def update_field(product_id):
	print("Start update_field: %s" % time.ctime())
	print("Product ID : %s" % product_id)
	time.sleep(20)
	job = get_object_or_404(Product.objects.all(), pk=product_id)
	job.status = 'Success'
	job.save()
	print("End update_field: %s" % time.ctime())
