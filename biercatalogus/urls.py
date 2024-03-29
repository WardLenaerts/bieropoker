from django.urls import path

from . import views

app_name = 'biercatalogus'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:id>/', views.product_detail, name='product_detail'),
    path('bierhier/<int:id>/', views.ik_wil, name='ik_wil'),
]