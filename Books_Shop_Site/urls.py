from django.urls import path, include
from Books_Shop_Site import views


app_name = 'Book_Shop_Site'


urlpatterns = [
    path('', views.index, name = 'index'),
    path('books-list/', views.BookClassView.as_view(), name = 'books-list'),
    path('book-details/<int:pk>/', views.BookClassDetails.as_view(), name = 'book-detail'),
]
