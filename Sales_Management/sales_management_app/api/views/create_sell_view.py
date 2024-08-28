from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from sales_management_app.api.models.sells_model import Sell
from sales_management_app.api.serializers.sells_serializer import SellSerializer

class CreateSellsView(APIView):
    def post(self, request, pk):
        data=request.data
        print("DATA",data)
        data['user']=pk
        
        serializer=SellSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
    
