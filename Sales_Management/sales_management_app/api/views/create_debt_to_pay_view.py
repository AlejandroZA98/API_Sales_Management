from sales_management_app.api.models.debts_to_pay_model import DebtstoPay
from sales_management_app.api.serializers.debts_to_pay_serializer import DebtstoPaySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CreateDebttoPay(APIView):
    def post(self,request,pk):
        data=request.data
        print("DATA",data)
        data['user']=pk
        
        serializer=DebtstoPaySerializer(data=data,context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)