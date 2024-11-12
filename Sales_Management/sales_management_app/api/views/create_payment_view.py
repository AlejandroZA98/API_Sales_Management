from rest_framework.views import APIView
from sales_management_app.api.models.payments_model import Payment
from sales_management_app.api.serializers.payments_serializer import PaymentSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class CreatePaymentsView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request, pk):
        data=request.data
        data['user']=pk
        
        serializer=PaymentSerializer(data=data,context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)