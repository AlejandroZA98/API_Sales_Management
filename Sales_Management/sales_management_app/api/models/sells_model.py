from django.db import models
from django.contrib.auth.models import User
from sales_management_app.api.models.clients_model import Client
from sales_management_app.api.models.products_model import Product

class Sell(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    client=models.ForeignKey(Client,on_delete=models.CASCADE)  
    concept=models.ManyToManyField(Product, related_name='sales')
    quantity=models.FloatField()
    type=models.CharField(max_length=30)
    unit_price=models.FloatField()
    price=models.FloatField()
    amount_paid=models.FloatField()
    settlement_date=models.DateTimeField(auto_now_add=True)
    debt_amount=models.FloatField()
    balance=models.FloatField()
    credits=models.FloatField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
         return self.type