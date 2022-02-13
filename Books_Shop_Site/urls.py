from django.urls import path, include
from Books_Shop_Site import views

urlpatterns = [
    path('', views.index, name = 'index'),
]
