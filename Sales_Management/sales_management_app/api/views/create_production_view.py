
from sales_management_app.api.models.production_model import Production
from sales_management_app.api.serializers.production_serializer import ProductionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CreateProductionView(APIView):
    def post(self, request,pk):
        data=request.data
        print("DATA",data)
        data['user']=pk
        serializer=ProductionSerializer(data=data,context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
    