from rest_framework.views import APIView
from sales_management_app.api.models.purchases_model import Purchase
from sales_management_app.api.serializers.purchases_serializer import PurchaseSerializer
from rest_framework.response import Response
from rest_framework import status

class PurchaseDetailView(APIView):
    def get(self, request, pk):
        try:
            purchase = Purchase.objects.get(pk=pk)
        except Purchase.DoesNotExist:
            return Response({'error':'Purchase not found'},status=status.HTTP_404_NOT_FOUND)
        serializer=PurchaseSerializer(purchase,context={'request': request})
        return Response(serializer.data)
    def put(self, request, pk):
        purchase=Purchase.objects.get(pk=pk)
        serializer=PurchaseSerializer(purchase,data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete (self,request,pk):
        purchase=Purchase.objects.get(pk=pk)
        purchase.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)