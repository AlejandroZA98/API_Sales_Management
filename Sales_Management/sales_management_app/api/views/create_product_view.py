from sales_management_app.api.models.products_model import Product
from sales_management_app.api.serializers.products_serializer import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class CreateProductView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request,pk):
        data=request.data
        data['user']=pk
        
        serializer=ProductSerializer(data=data,context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
    
