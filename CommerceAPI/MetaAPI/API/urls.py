from django.urls import path
from . import views

urlpatterns = [
    path('menuitems/', views.MenuItemView.as_view()),
    path('menuitems/<int:pk>', views.SingleMenuItemView.as_view()),
]
