from rest_framework import serializers
from sales_management_app.api.models.debts_to_pay_model import DebtstoPay 
from django.contrib.auth.models import User

class DebtstoPaySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many=False)  # Permitir el ID del usuario
    #user= serializers.StringRelatedField(read_only=True)
    user_name = serializers.StringRelatedField(source='user', read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='debtstopay-detail')
    class Meta:
        model=DebtstoPay
        fields='__all__'
        #exclude=('user',)
        
        