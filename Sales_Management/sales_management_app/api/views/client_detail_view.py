from rest_framework.views import APIView
from sales_management_app.api.models.clients_model import Client
from sales_management_app.api.serializers.clients_serializer import ClientSerializer
from rest_framework.response import Response
from rest_framework import status

class ClientDetailView(APIView):
    def get(self, request,pk):
        try:
            client = Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            return Response({'error':'Client not found'},status=status.HTTP_404_NOT_FOUND)
        serializer=ClientSerializer(client,context={'request': request})
        return Response(serializer.data)
    def put(self, request,pk):
        client=Client.objects.get(pk=pk)
        serializer=ClientSerializer(client,data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        client=Client.objects.get(pk=pk)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)