from rest_framework import mixins, generics
from sales_management_app.api.models.clients_model import Client
from sales_management_app.api.serializers.clients_serializer import ClientSerializer

class ClientsView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)