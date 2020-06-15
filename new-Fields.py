## first delete all files in migrations( except for __init__.py) folder an sql database 

## becasue you delete database ; you need to create super user again

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser


## changes in models.py

from django.db import models

# Create your models here.
class Product(models.Model):
 titel       = models.CharField(max_length=120) 
 description = models.TextField(blank = True , null = True)
 price       = models.DecimalField(decimal_places = 2, max_digits = 1000 )
 summary     = models.TextField()
