
from sales_management_app.api.models.production_model import Production
from sales_management_app.api.serializers.production_serializer import ProductionSerializer
from sales_management_app.api.models.inventary_ingredients_model import InventaryIngredients
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CreateProductionView(APIView):
    def post(self, request,pk):
        data=request.data
        ingredients=request.data.get('ingredients')
        print("INGREDIENTS",ingredients)
        print("DATA",data)
        data['user']=pk
        serializer=ProductionSerializer(data=data,context={'request':request})
      
        for ingredient in ingredients:
            print("QUANTITY",ingredient['cuantity'])
            try:
                inventory_item = InventaryIngredients.objects.get(ingredient=ingredient['ingredient'])
                print("inventory",inventory_item)

                if inventory_item.cuantity < ingredient['cuantity']:
                    return Response(
                        {"error": f"El ingrediente '{ingredient['ingredient']}' no tiene suficiente stock."}, 
                        status=400)
                inventory_item.cuantity -= ingredient['cuantity']*data['cuantity']
                inventory_item.save()
                if serializer.is_valid():
                    serializer.save()

            except InventaryIngredients.DoesNotExist:
                return Response(
                {"error": f"El ingrediente '{ingredient['ingredient']}' no se encuentra en el inventario."}, 
                status=400)

        return Response({
                'status': 'success',
                'message': 'Produccion registrada y stock actualizado.',}, status=status.HTTP_201_CREATED)