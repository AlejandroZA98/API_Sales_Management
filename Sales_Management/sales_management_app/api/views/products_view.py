from rest_framework import mixins, generics
from sales_management_app.api.models.products_model import Product
from sales_management_app.api.serializers.products_serializer import ProductSerializer

class ProductView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    