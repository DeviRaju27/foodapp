from django.contrib import admin
from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    #index /menu/
    path('',views.IndexClassView.as_view(), name="index" ),
    #eachitemdetail /menu/1
    path('<int:pk>',views.DetailView.as_view(), name="detail" ),
    path('add', views.CreateItem.as_view(), name="add_item" ),
    path('update/<int:id>', views.update_item, name = 'update_item'),
    path('delete/<int:id>', views.delete_item, name = 'delete_item'),
]