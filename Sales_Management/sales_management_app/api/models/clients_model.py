from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=120)
    paid_money=models.FloatField()
    debt_money=models.FloatField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
         return self.name