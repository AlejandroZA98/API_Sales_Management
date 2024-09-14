from rest_framework import serializers
from sales_management_app.api.models.payments_model import Payment 
from django.contrib.auth.models import User
from sales_management_app.api.models.clients_model import Client

class PaymentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many=False)  # Permitir el ID del usuario
    user_name = serializers.StringRelatedField(source='user', read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='payment-detail')
    client =serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), many=False)  # Corrección aquí

    client_name = serializers.StringRelatedField(source='client', read_only=True)
    class Meta:
        model=Payment
        fields='__all__'
        
        