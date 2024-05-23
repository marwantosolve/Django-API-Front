from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("get/", views.get, name = "get"),
    path("post/", views.post, name = "post"),
    path("put/", views.put, name = "put"),
    path("delete/", views.delete, name = "delete"),
    path('books/', views.book_list),
    path('books/<int:id>/', views.book_detail),
]