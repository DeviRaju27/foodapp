from django.contrib import admin
from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    path('/',views.index, name="index" ),
    path('<int:item_id>',views.detail, name="detail" ),
    path('/add', views.add_item, name="add_item" ),
]