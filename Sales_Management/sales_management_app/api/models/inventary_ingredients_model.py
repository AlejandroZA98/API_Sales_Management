from django.db import models
from django.contrib.auth.models import User

class InventaryIngredients(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    ingredient=models.CharField(max_length=120)
    cuantity=models.FloatField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
         return str(self.ingredient)