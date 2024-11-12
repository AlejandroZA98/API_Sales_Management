from sales_management_app.api.models.debts_to_pay_model import DebtstoPay
from sales_management_app.api.serializers.debts_to_pay_serializer import DebtstoPaySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class DebtstoPayDetailView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request, pk):
        try:
            debttopay=DebtstoPay.objects.get(pk=pk)
        except DebtstoPay.DoesNotExist:
            return Response({'error':'Debt to Pay not found'},status=status.HTTP_404_NOT_FOUND)
        serializer=DebtstoPaySerializer(debttopay,context={'request': request})
        return Response(serializer.data)
    def put (self, request, pk):
        debttopay=DebtstoPay.objects.get(pk=pk)
        serializer=DebtstoPaySerializer(debttopay,data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete (self,request,pk):
        debttopay=DebtstoPay.objects.get(pk=pk)
        debttopay.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)