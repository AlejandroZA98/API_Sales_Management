from rest_framework.views import APIView
from sales_management_app.api.models.products_model import Product
from sales_management_app.api.serializers.products_serializer import ProductSerializer
from rest_framework.response import Response
from rest_framework import status

class ProductDetailView(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return Response({'error':'Client not found'},status=status.HTTP_404_NOT_FOUND)
        serializer=ProductSerializer(product,context={'request': request})
        return Response(serializer.data)
    def put(self, request, pk):
        product=Product.objects.get(pk=pk)
        serializer=ProductSerializer(product,data=request.data,context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
