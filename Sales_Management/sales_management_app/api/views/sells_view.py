from rest_framework import mixins, generics
from sales_management_app.api.models.sells_model import Sell
from sales_management_app.api.serializers.sells_serializer import SellSerializer
from rest_framework import filters

class SellsView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer
    filter_backends = [filters.SearchFilter]
    search_fields=['client__name','debt_amount']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)