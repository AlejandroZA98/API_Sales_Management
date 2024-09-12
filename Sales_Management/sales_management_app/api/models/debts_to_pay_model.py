from django.db import models
from django.contrib.auth.models import User

class DebtstoPay(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    amount_sell=models.FloatField()
    amount_paid=models.FloatField()
    debt=models.FloatField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.debt)