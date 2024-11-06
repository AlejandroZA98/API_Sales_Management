
from sales_management_app.api.models.clients_model import Client
from sales_management_app.api.serializers.clients_serializer import ClientSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CreateClientsView(APIView):
    def post(self, request,pk):
        data=request.data
        data['user']=pk
        
        serializer=ClientSerializer(data=data,context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
    
