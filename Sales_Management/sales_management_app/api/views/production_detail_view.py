from sales_management_app.api.models.production_model import Production
from sales_management_app.api.serializers.production_serializer import ProductionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ProductionDetailView(APIView):
    def get(self, request, pk):
        try:
            production = Production.objects.get(pk=pk)
        except Production.DoesNotExist:
            return Response({'error':'Production not found'},status=status.HTTP_404_NOT_FOUND)
        serializer=ProductionSerializer(production,context={'request': request})
        return Response(serializer.data)
    def put(self, request,pk):
        client=Production.objects.get(pk=pk)
        serializer=ProductionSerializer(client,data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        client=Production.objects.get(pk=pk)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)