from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="/"),
    path('add-product/', views.addProduct, name="add-prod"),  
    path('edit-product/<str:pk>', views.editProduct, name="edit-prod"),
    path('delete-product/<str:pk>', views.deleteProduct, name="delete-prod")
]