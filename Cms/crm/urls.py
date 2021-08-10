from django.urls import path
from crm import views

urlpatterns=[
    path('employees/add',views.emp_add),
    path('employees/view/<int:id>',views.emp_view),
    path('employees/change/<int:id>',views.emp_update),
    path('employees/remove/<int:id>',views.emp_delete),
    path('employees',views.emp_details)
]
