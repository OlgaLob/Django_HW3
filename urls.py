from django.urls import path
from internet_shop import views
from internet_shop.views import basket, sorted_basket

urlpatterns = [
    path('clients/', views.get_clients, name='clients'),
    path('goods/', views.get_goods, name='goods'),
    path('orders/', views.get_orders, name='orders'),
    path('client_orders/<int:client_id>', views.get_orders_by_client_id, name='client_orders'),
    path('user/<int:user_id>/', basket, name='basket'),
    path('user_sorted/<int:user_id>/<int:days_ago>/', sorted_basket, name='sorted_basket'),
]