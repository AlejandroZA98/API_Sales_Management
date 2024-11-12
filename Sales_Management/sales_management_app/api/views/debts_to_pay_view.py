from rest_framework import mixins, generics
from sales_management_app.api.models.debts_to_pay_model import DebtstoPay
from sales_management_app.api.serializers.debts_to_pay_serializer import DebtstoPaySerializer
from rest_framework import filters

class DebtstoPayView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = DebtstoPay.objects.all()
    serializer_class = DebtstoPaySerializer
    filter_backends = [filters.SearchFilter]
    search_fields=['client__name','amount_sell']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    