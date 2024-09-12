from django.db import models
from django.contrib.auth.models import User

class Payment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date =models.DateTimeField()
    amount=models.FloatField()
    merchandise=models.CharField(max_length=150)
    note=models.TextField(blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
         return str(self.amount)
