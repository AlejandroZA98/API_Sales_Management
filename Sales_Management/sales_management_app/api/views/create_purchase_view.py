from sales_management_app.api.models.purchases_model import Purchase
from sales_management_app.api.models.inventary_ingredients_model import InventaryIngredients
from sales_management_app.api.serializers.purchases_serializer import PurchaseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CreatePurchaseView(APIView):
    def post(self, request, pk):
        products_data = request.data 
        print("DATA", products_data)
        
        purchases_created = []  
        
        try:
            for product_data in products_data:
                product_data['user'] = pk  

                purchase = Purchase.objects.create(
                    user_id=product_data['user'],
                    concept=product_data['concept'],
                    cuantity=product_data['cuantity'],
                    unit_price=product_data['unit_price'],
                    total_amount=product_data['cuantity'] * product_data['unit_price'],
                    type=product_data['type'],
                    balance=product_data['balance'],
                    supplier=product_data['supplier'],
                )

                inventory_item, created = InventaryIngredients.objects.get_or_create(
                    ingredient=product_data['concept'],
                    user_id=product_data['user'], 
                    defaults={'cuantity': 0} 
                )

                inventory_item.cuantity += product_data['cuantity']
                inventory_item.save()

                purchases_created.append(purchase.id) 

            return Response({
                'status': 'success',
                'message': 'Compras registradas y stock actualizado.',
                'purchases_created': purchases_created
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
