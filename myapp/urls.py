from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", views.index, name="index"),
    path("get/", views.get, name = "get"),
    path('books/', views.book_list),
    path('books/<int:id>/', views.book_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)