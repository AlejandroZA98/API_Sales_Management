from django.db import models
from django.contrib.auth.models import User
from sales_management_app.api.models.clients_model import Client

class DebtstoPay(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    client=models.ForeignKey(Client,on_delete=models.CASCADE)  
    amount_sell=models.FloatField()
    amount_paid=models.FloatField()
    debt=models.FloatField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.debt)