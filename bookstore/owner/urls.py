from django.urls import path
from owner import views
urlpatterns=[
    path("books/add",views.book_create,name="addbook"),
    path("books/list",views.book_list,name="listbook"),
    path("books/change/<int:id>",views.book_update,name="changebook"),
    path("books/remove/<int:id>",views.book_remove,name="removebook")
]