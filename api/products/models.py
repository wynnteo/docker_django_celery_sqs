from django.db import models

# Create your models here.
class Product(models.Model):
	title = models.TextField()
	description = models.TextField()
	price = models.DecimalField(max_digits=5, decimal_places=2)
	modified_date = models.DateTimeField(auto_now=True)
	created_date = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = "product"

