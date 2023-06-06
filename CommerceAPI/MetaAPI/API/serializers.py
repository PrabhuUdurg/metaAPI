from rest_framework import serializers
from .models import MenuItem, Category, Cart, Order, OrderItem
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'featured', ]
        

class CartSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Cart 
        fields = ['user', 'menuitem', 'quantity', 'unit_price', 'price']
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'items', 'total', 'status', 'ordered_date', 'ordered_time', 'completed_date', 'completed_time', 'cancelled_date', 'cancelled_time'] 