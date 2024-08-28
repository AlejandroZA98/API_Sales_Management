from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from sales_management_app.api.models.sells_model import Sell
from sales_management_app.api.serializers.sells_serializer import SellSerializer

class SellDetailView(APIView):
    def get(self, request, pk):
        try:
            sell = Sell.objects.get(id=pk)
        except Sell.DoesNotExist:
            return Response({'error':'Sell not found'},status=status.HTTP_404_NOT_FOUND)
        
        serializer = SellSerializer(sell,context={'request': request})
        return Response(serializer.data)
    def put(self, request, pk):
        sell = Sell.objects.get(id=pk)
        serializer = SellSerializer(sell, data=request.data,context={'request': request})
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        sell=Sell.objects.get(pk=pk)
        sell.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)