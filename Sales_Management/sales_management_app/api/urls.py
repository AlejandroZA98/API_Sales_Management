from django.contrib import admin
from django.urls import path,include
from sales_management_app.api.views.clients_view import ClientsView
from sales_management_app.api.views.create_clients_view import CreateClientsView
from sales_management_app.api.views.products_view import ProductView
from sales_management_app.api.views.create_product_view import CreateProductView
from sales_management_app.api.views.client_detail_view import ClientDetailView
from sales_management_app.api.views.products_detail_view import ProductDetailView
from sales_management_app.api.views.purchases_view import PurchasesView
from sales_management_app.api.views.create_purchase_view import CreatePurchaseView
from sales_management_app.api.views.purchases_detail_view import PurchaseDetailView
from sales_management_app.api.views.sells_view import SellsView
from sales_management_app.api.views.create_sell_view import CreateSellsView
from sales_management_app.api.views.sell_detail_view import SellDetailView
from sales_management_app.api.views.productions_view import ProductionView
from sales_management_app.api.views.create_production_view import CreateProductionView
from sales_management_app.api.views.production_detail_view import ProductionDetailView
from sales_management_app.api.views.payments_view import PaymentsView
from sales_management_app.api.views.create_payment_view import CreatePaymentsView
from sales_management_app.api.views.payment_detail_view import PaymentDetailView
from sales_management_app.api.views.debts_to_pay_view import DebtstoPayView
from sales_management_app.api.views.create_debt_to_pay_view import CreateDebttoPay
from sales_management_app.api.views.debts_to_pay_detail_view import DebtstoPayDetailView

urlpatterns = [
    path('clients/',ClientsView.as_view(),name='clients'),
    path('<int:pk>/create-clients/',CreateClientsView.as_view(),name='create-clients'),
    path('client-detail/<int:pk>/',ClientDetailView.as_view(),name='client-detail'),
    path('products/',ProductView.as_view(),name='products'),
    path('<int:pk>/create-products/',CreateProductView.as_view(),name='create-products'),
    path('product-detail/<int:pk>/',ProductDetailView.as_view(),name='product-detail'),
    path('purchases/',PurchasesView.as_view(),name='purchases'),
    path('<int:pk>/create-purchase/',CreatePurchaseView.as_view(),name='create-purchase'),
    path('purchase-detail/<int:pk>/',PurchaseDetailView.as_view(),name='purchase-detail'),
    path('sells/',SellsView.as_view(),name='sells'),
    path('<int:pk>/create-sell/',CreateSellsView.as_view(),name='create-sell'),
    path('sell-detail/<int:pk>/',SellDetailView.as_view(),name='sell-detail'),
    path('productions/',ProductionView.as_view(),name='productions'),
    path('<int:pk>/create-production/',CreateProductionView.as_view(),name='create-production'),
    path('production-detail/<int:pk>/',ProductionDetailView.as_view(),name='production-detail'),
    path('payments/',PaymentsView.as_view(),name='payments'),
    path('<int:pk>/create-payment/',CreatePaymentsView.as_view(),name='create-payment'),
    path('payment-detail/<int:pk>/',PaymentDetailView.as_view(),name='payment-detail'),
    path('debtstopay/',DebtstoPayView.as_view(),name='debtstopay'),
    path('<int:pk>/create-debttopay/',CreateDebttoPay.as_view(),name='create-debttopay'),
    path('debtstopay-detail/<int:pk>/',DebtstoPayDetailView.as_view(),name='debtstopay-detail'),

]
