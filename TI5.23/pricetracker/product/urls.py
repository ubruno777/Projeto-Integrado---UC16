from django.urls import path
from . import views

# <int:codprod> é como um "filtro" / recorte de determinado parâmetro 
urlpatterns = [
    path('saveprod/', views.saveprod, name='saveprod'),
    path('saveprice/', views.saveprice, name='saveprice'),
    path('historyprice/<int:codprod>/', views.historyprice, name='historyprice'),
    path('productlist/', views.productlist, name='productlist' ),
    path('pricechart/<int:codprod>/', views.pricechart, name='pricechart')
]