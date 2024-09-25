from sales_management_app.api.models.production_model import Production
from sales_management_app.api.serializers.production_serializer import ProductionSerializer
from sales_management_app.api.models.inventary_ingredients_model import InventaryIngredients
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
  
    def delete(self, request, pk):
        try:
            production = Production.objects.get(pk=pk)
            print("PRODUCTION",production.ingredients,production.cuantity)

            ingredients=production.ingredients
            for ingredient in ingredients:
                print("INGER",ingredient['ingredient'],ingredient['cuantity'])
                inventory_item = InventaryIngredients.objects.get(ingredient=ingredient['ingredient'])
                print("inventory_item",inventory_item.cuantity)
                inventory_item.cuantity += ingredient['cuantity']*production.cuantity
                print("inventory_item",inventory_item.cuantity)

                inventory_item.save()

        except Production.DoesNotExist:
            return Response({'error': 'production not found'}, status=status.HTTP_404_NOT_FOUND)

        production.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)