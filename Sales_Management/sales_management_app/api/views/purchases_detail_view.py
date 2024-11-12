from rest_framework.views import APIView
from sales_management_app.api.models.purchases_model import Purchase
from sales_management_app.api.serializers.purchases_serializer import PurchaseSerializer
from sales_management_app.api.models.inventary_ingredients_model import InventaryIngredients
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class PurchaseDetailView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request, pk):
        try:
            purchase = Purchase.objects.get(pk=pk)
        except Purchase.DoesNotExist:
            return Response({'error':'Purchase not found'},status=status.HTTP_404_NOT_FOUND)
        serializer=PurchaseSerializer(purchase,context={'request': request})
        return Response(serializer.data)
   
    def delete(self, request, pk):
        try:
            purchase = Purchase.objects.get(pk=pk)
        except Purchase.DoesNotExist:
            return Response({'error': 'Purchase not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
            inventory_item = InventaryIngredients.objects.get(
                ingredient=purchase.concept,
                user_id=purchase.user.id
            )
            
            inventory_item.cuantity -= purchase.cuantity
            
            if inventory_item.cuantity <= 0:
                inventory_item.delete()
            else:
                inventory_item.save()  

        except InventaryIngredients.DoesNotExist:
            
            pass  

        purchase.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
