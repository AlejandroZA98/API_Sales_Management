from sales_management_app.api.models.production_model import Production
from sales_management_app.api.serializers.production_serializer import ProductionSerializer
from sales_management_app.api.models.inventary_ingredients_model import InventaryIngredients
from sales_management_app.api.models.inventary_products_model import InventaryProducts
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class CreateProductionView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request, pk):
        data = request.data
        ingredients = data.get('ingredients')

        data['user'] = pk
        
        serializer = ProductionSerializer(data=data, context={'request': request})

        for ingredient_name, required_quantity in ingredients.items():
            try:
                inventory_item = InventaryIngredients.objects.get(ingredient=ingredient_name)

                if inventory_item.cuantity < required_quantity * data['cuantity']:
                    return Response(
                        {"error": f"El ingrediente '{ingredient_name}' no tiene suficiente stock."}, 
                        status=status.HTTP_400_BAD_REQUEST)

                inventory_item.cuantity -= required_quantity * data['cuantity']
                inventory_item.save()

            except InventaryIngredients.DoesNotExist:
                return Response(
                    {"error": f"El ingrediente '{ingredient_name}' no se encuentra en el inventario."}, 
                    status=status.HTTP_400_BAD_REQUEST)
        
        if serializer.is_valid():
            inventory_item, created = InventaryProducts.objects.get_or_create(
                    product=data['concept'],
                    user=User.objects.get(pk=pk), 
                    defaults={'cuantity': 0} 
                )
            inventory_item.cuantity += data['cuantity']
            inventory_item.save()

            serializer.save()
            return Response({
                'status': 'success',
                'message': 'Producción registrada y stock actualizado.',
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
