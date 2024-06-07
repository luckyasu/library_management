from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index),
    path('login/', views.login, name='login'),
    path('add_publisher/', views.add_publisher, name='add_publisher'),
    path('publisher_list/', views.publisher_list, name='publisher_list'),
    path('edit_publisher/', views.edit_publisher, name='edit_publisher'),
    path('delete_publisher/', views.delete_publisher, name='delete_publisher'),
    path('add_book/', views.add_book, name='add_book'),
    path('book_list/', views.book_list, name='book_list'),
    path('edit_book/', views.edit_book, name='edit_book'),
    path('delete_book/', views.delete_book, name='delete_book'),
    path('add_author/', views.add_author, name='add_author'),
    path('edit_author/', views.edit_author, name='edit_author'),
    path('delete_author/', views.delete_author, name='delete_author'),
    path('author_list/', views.author_list, name='author_list'),
    path('logout/', views.logout, name='logout'),
]
