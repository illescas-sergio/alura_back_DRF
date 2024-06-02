from django.db import models
from django.contrib.auth import get_user_model
import uuid

# Create your models here.

class Product(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=50)
    product_description = models.CharField(max_length=250)
    category = models.CharField(max_length=50, blank=True)
    price = models.FloatField()
    product_image = models.ImageField(blank=True, null=True, upload_to='productos/')
    product_owner = models.ForeignKey(to=get_user_model(), related_name = 'published_products', on_delete=models.CASCADE)


    def __str__(self):
        
        return self.product_name
