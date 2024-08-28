from sales_management_app.api.models.purchases_model import Purchase
from sales_management_app.api.serializers.purchases_serializer import PurchaseSerializer
from rest_framework import mixins, generics



class PurchasesView(mixins.ListModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    