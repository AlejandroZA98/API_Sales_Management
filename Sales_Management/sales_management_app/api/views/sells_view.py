from rest_framework import mixins, generics
from sales_management_app.api.models.sells_model import Sell
from sales_management_app.api.serializers.sells_serializer import SellSerializer

class SellsView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)