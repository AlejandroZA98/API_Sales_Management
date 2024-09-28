from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from sales_management_app.api.models.sells_model import Sell
from sales_management_app.api.models.products_model import Product
from sales_management_app.api.models.inventary_products_model import InventaryProducts
from django.shortcuts import get_object_or_404

class CreateSellsView(APIView):
    def post(self, request, pk):
        data = request.data
        print("DATA", data)
        data['user'] = pk

        try:
            concept_ids = data.get('concept', [])
            quantities = data.get('details', {}).get('quantities', [])

            if len(concept_ids) != len(quantities):
                return Response({'error': 'La cantidad de conceptos no coincide con la de cantidades.'}, status=status.HTTP_400_BAD_REQUEST)

            total_price = 0

            sell = Sell.objects.create(
                user_id=data['user'],
                client_id=data['client'],
                type=data.get('type', ''),
                amount_paid=data.get('amount_paid', 0),
                debt_amount=data.get('debt_amount', 0),
                balance=data.get('balance', 0),
                credits=data.get('credits', 0),
                details={}  
            )
            details_content = {}
            for index, concept_id in enumerate(concept_ids):
                quantity = quantities[index]
                product = get_object_or_404(Product, id=concept_id)
                inventory_item = get_object_or_404(InventaryProducts, product=product.name)
                if inventory_item.cuantity < quantity:
                    return Response(
                        {'error': f"No hay suficiente stock para el producto '{product.name}'."},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                inventory_item.cuantity -= quantity
                inventory_item.save()
                
                total_price += quantity * product.unit_price

                details_content[f"{concept_id}"] = {
                    'quantity': quantity,
                    'price_unit': product.unit_price
                }

            sell.details = details_content
            sell.total_price = total_price  
            sell.save()
            sell.concept.set(concept_ids)
            sell.save()

            return Response({'id': sell.id, 'total_price': total_price}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
