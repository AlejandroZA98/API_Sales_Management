from django.db import models
from django.contrib.auth.models import User

class Purchase(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    concept=models.CharField(max_length=120)
    cuantity=models.FloatField()
    unit_price=models.FloatField()
    total_amount=models.FloatField()
    type=models.CharField(max_length=50)
    balance=models.FloatField()
    supplier=models.CharField(max_length=120)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
         return str(self.concept)