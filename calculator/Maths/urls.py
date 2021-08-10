from django.urls import path
from Maths import views

urlpatterns=[
    path('addnum',views.add_numbers,name="addnums"),
    path('subnum',views.sub_numbers,name="subnums"),
    path('mulnum',views.mul_numbers,name="mulnums"),
    path('divnum',views.div_numbers,name="divnums"),
    path('cube',views.cube,name="cubenum")
]