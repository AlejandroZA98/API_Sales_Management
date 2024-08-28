from rest_framework import serializers
from sales_management_app.api.models.production_model import Production
from django.contrib.auth.models import User

class ProductionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many=False)
    user_name = serializers.StringRelatedField(source='user', read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='production-detail')
    class Meta:
        model=Production
        fields='__all__'