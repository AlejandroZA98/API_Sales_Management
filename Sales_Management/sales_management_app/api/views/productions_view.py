from rest_framework import mixins, generics
from sales_management_app.api.models.production_model import Production
from sales_management_app.api.serializers.production_serializer import ProductionSerializer

class ProductionView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Production.objects.all()
    serializer_class = ProductionSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    