from django.urls import path
from . import views

# <int:codprod> é como um "filtro" / recorte de determinado parâmetro
urlpatterns = [
    path('saveprod/', views.saveprod, name='saveprod'),
    path('saveprice/', views.saveprice, name='saveprice'),
    path('historyprice/<int:product_id>/', views.historyprice, name='historyprice'),
    path('productlist/', views.productlist, name='productlist'),
    path('pricechart/<int:codprod>/', views.pricechart, name='pricechart'),
    path('editproduct/<int:codprod>/', views.editproduct, name='editproduct'),
    path('deleteproduct/<int:codprod>/', views.deleteproduct, name='deleteproduct'),
    path('alterar/<int:codprice>/', views.alterar, name='alterar'),
    path('deleteprice/<int:codprice>/', views.deleteprice, name='deleteprice'),
]