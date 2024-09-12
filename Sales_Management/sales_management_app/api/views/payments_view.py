from rest_framework import mixins, generics
from sales_management_app.api.models.payments_model import Payment
from sales_management_app.api.serializers.payments_serializer import PaymentSerializer
from rest_framework.response import Response
from rest_framework import status

class PaymentsView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    