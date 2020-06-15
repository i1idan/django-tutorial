## make sure you are in right path

manage.py startapp products


## go to product folder find models.py add following codes an save script

from django.db import models

# Create your models here.

class Product(models.Model):
	title       = models.TextField()
	description = models.TextField()
	price       = models.TextField()
	summary     = models.TextField(default="this is cool!")
  
  
  ## go to admins.py and dd following codes an save script
  from django.contrib import admin

  # Register your models here.

  from .models import Product

  admin.site.register(Product)

 ## go back to terminal 
 
 python manage.py makemigrations
 python manage.py migrate
  
 ## now in the url you can see products add products and make change to them
 
 http://127.0.0.1:8000/admin/

 
