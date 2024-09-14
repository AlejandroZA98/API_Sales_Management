from rest_framework import serializers
from sales_management_app.api.models.sells_model import Sell 
from django.contrib.auth.models import User
from sales_management_app.api.models.clients_model import Client

class SellSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many=False)  # Permitir el ID del usuario
    user_name = serializers.StringRelatedField(source='user', read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='sell-detail')
    client=serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(),many=False)
    client_name = serializers.StringRelatedField(source='client', read_only=True)
    class Meta:
        model= Sell
        fields='__all__'    