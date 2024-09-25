from django.db import models
from django.contrib.auth.models import User


class Production(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    concept=models.CharField(max_length=120)
    cuantity=models.FloatField()
    ingredients=models.JSONField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
         return str(self.concept)
