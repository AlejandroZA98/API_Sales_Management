from rest_framework import mixins, generics
from sales_management_app.api.models.clients_model import Client
from sales_management_app.api.serializers.clients_serializer import ClientSerializer
from rest_framework import filters

class ClientsView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [filters.SearchFilter]
    search_fields=['name']
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)