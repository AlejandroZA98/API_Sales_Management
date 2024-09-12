from rest_framework.views import APIView
from sales_management_app.api.models.payments_model import Payment
from sales_management_app.api.serializers.payments_serializer import PaymentSerializer
from rest_framework.response import Response
from rest_framework import status


class PaymentDetailView(APIView):
    def get(self ,request,pk):
        try:
            payment= Payment.objects.get(pk=pk)
        except Payment.DoesNotExist:
            return Response({'error':'Payment not found'},status=status.HTTP_404_NOT_FOUND)
        serializer=PaymentSerializer(payment,context={'request': request})
        return Response(serializer.data)
    def put (self ,request,pk):
        payment=Payment.objects.get(pk=pk)
        serializer=PaymentSerializer(payment,data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
