from django.db import models

class Payment(models.Model):
    date =models.DateTimeField()
    amount=models.FloatField()
    merchandise=models.CharField(max_length=150)
    note=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
         return str(self.amount)
