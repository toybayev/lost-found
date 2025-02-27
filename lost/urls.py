from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('item/<int:id>/', views.detail, name='item-detail'),
    path('item/new/', views.create, name='item-create'),
    path('item/<int:id>/edit/', views.update, name='item-edit'),
    path('item/<int:id>/delete/', views.delete, name='item-delete'),
]
