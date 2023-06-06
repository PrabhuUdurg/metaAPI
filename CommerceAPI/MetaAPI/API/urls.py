from django.urls import path
from . import views

urlpatterns = [
    path('menuitems/', views.MenuItemView.as_view()),
    path('menuitems/<int:pk>', views.SingleMenuItemView.as_view()),
    path('cart/menuitems', views.CartView.as_view()),
    path('orders/', views.OrderView.as_view()),
    path('orders/<int:pk>', views.SingleOrderView.as_view()),
    
]

