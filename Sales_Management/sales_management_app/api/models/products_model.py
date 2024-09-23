from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=120)
    unit_price=models.FloatField()
    type=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):

         return self.name 