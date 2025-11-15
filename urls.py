from django.urls import path
from .views import (
    home, toy_list, toy_detail, signup_view,
    view_cart, add_to_cart, remove_from_cart,
    checkout, category_list, toys_by_category
)

urlpatterns = [
    path('', home, name='home'),
    path('toys/', toy_list, name='toy_list'),
    path('toys/<int:toy_id>/', toy_detail, name='toy_detail'),
    path('signup/', signup_view, name='signup'),
    path('cart/', view_cart, name='view_cart'),
    path('add_to_cart/<int:toy_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/', checkout, name='checkout'),
    path('categories/', category_list, name='category_list'),
    path('category/<int:category_id>/', toys_by_category, name='category'),
]
