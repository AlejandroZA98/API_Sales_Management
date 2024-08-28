from rest_framework import serializers
from sales_management_app.api.models.purchases_model import Purchase
from django.contrib.auth.models import User

class PurchaseSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many=False)  # Permitir el ID del usuario
    user_name = serializers.StringRelatedField(source='user', read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='purchase-detail')

    class Meta:
        model=Purchase
        fields='__all__'