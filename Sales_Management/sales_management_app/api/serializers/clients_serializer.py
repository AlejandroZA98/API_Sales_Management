from rest_framework import serializers
from sales_management_app.api.models.clients_model import Client 
from django.contrib.auth.models import User

class ClientSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many=False)  # Permitir el ID del usuario
    #user= serializers.StringRelatedField(read_only=True)
    user_name = serializers.StringRelatedField(source='user', read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='client-detail')
    class Meta:
        model=Client
        fields='__all__'
        #exclude=('user',)
        
        