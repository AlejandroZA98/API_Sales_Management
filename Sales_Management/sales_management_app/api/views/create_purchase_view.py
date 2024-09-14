from sales_management_app.api.models.purchases_model import Purchase
from sales_management_app.api.serializers.purchases_serializer import PurchaseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CreatePurchaseView(APIView):
    def post(self, request,pk):
        data=request.data
        print("DATA",data)
        data['user']=pk
        
        serializer=PurchaseSerializer(data=data,context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
    
