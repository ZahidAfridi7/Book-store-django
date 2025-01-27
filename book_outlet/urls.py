from django.urls import path

from . import views

urlpatterns = [
    path("",views.index),
    path("book_outlet/<int:id>", views.book_details , name="book-detail")
]