from django.contrib import admin
from sales_management_app.api.models.clients_model import Client
from sales_management_app.api.models.sells_model import Sell
from sales_management_app.api.models.purchases_model import Purchase
from sales_management_app.api.models.products_model import Product
from sales_management_app.api.models.payments_model import Payment
from sales_management_app.api.models.debts_to_pay_model import DebtstoPay
from sales_management_app.api.models.production_model import Production

# Register your models here.
admin.site.register(Client)
admin.site.register(Sell)
admin.site.register(Purchase)
admin.site.register(Product)
admin.site.register(Payment)
admin.site.register(DebtstoPay)
admin.site.register(Production)
