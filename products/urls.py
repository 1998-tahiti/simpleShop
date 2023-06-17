from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:product_id>/', views.detail, name='detail'),
    path('addProduct/', views.addProduct, name="addProduct"),
    path('NewAdded/', views.NewAdded, name="NewAdded"),
]