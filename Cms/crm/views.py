from django.shortcuts import render

# Create your views here.

# 8000/crm/employees
def emp_details(request):
    return render(request,'employees.html')
# 8000/crm/employees/add
def emp_add(request):
    return render(request,'add_emp.html')

# 8000/crm/employees/view
def emp_view(request,id):
    return render(request,'view_empdetails.html')

# 8000/crm/employees/change
def emp_update(request,id):
    return render(request,'change_emp.html')

# 8000/crm/employees/remove
def emp_delete(request,id):
    return render(request,'remove_emp.html')
