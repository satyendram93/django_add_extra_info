from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Employee

def home_view(request):
    return render(request, 'myapp/home.html')

def employee_list_view(request):
    employees = Employee.objects.all().order_by('-id')
    context={
        'employees': employees,
    }
    return render(request, 'myapp/employee_list.html', context)

# import pdb
def employee_create_view(request):
    """Render a form to create an employee and save extra fields dynamically."""
    if request.method == "POST":
        # pdb.set_trace()
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")

        # Retrieve extra fields as key-value pairs
        extra_keys = request.POST.getlist("extra_key[]")
        extra_values = request.POST.getlist("extra_value[]")
        extra_info = {key: value for key, value in zip(extra_keys, extra_values) if key and value}

        # Create employee record
        Employee.objects.create(name=name, email=email, age=age, extra_info=extra_info)
        return redirect("employee-list")  # Redirect to employee list

    return render(request, "myapp/employee_create.html")

def employee_update_view(request, pk):
    employee = get_object_or_404(Employee, id=pk)

    if request.method == "POST":

        # Update basic fields
        employee.name = request.POST.get('name')
        employee.email = request.POST.get('email')
        employee.age = request.POST.get('age')

        ## Process extra fields
        extra_keys = request.POST.getlist("extra_key[]")
        extra_values = request.POST.getlist("extra_value[]")
        employee.extra_info = {key:value for key,value in zip(extra_keys,extra_values) if key and value}

        #Save updates
        employee.save()
        return redirect('employee-list')
    context = {
        'employee': employee,
    }
    return render(request, 'myapp/employee_update.html', context)


def employee_delete_view(request, pk):
    ids = get_object_or_404(Employee, id=pk)
    ids.delete()
    return redirect('employee-list')