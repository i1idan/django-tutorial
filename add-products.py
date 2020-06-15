python manage.py shell

from products.models import Product

Product.objects.create(title='new product 1',description='another one',price='689',summary='sweet')


Product.objects.all()
<QuerySet [<Product: Product object (1)>, <Product: Product object (2)>, <Product: Product object (3)>, <Product: Product object (4)>, <Product: Product object (5)>, <Product: Product object (6)>, <Product: Product object (7)>]>
