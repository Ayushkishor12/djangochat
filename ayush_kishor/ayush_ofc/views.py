from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q  # Fixed incorrect import

# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'view_all_emp.html', context)

def add_emp(request):
    if request.method == 'POST':
        try:
            first_name = request.POST.get('first_name', '').strip()
            last_name = request.POST.get('last_name', '').strip()
            salary = float(request.POST.get('salary', 0))
            bonus = float(request.POST.get('bonus', 0))
            phone = request.POST.get('phone', '').strip()
            dept_id = request.POST.get('dept', '').strip()
            role_id = request.POST.get('role', '').strip()

            # Validate and fetch related department and role objects
            try:
                dept = Department.objects.get(id=dept_id)
            except Department.DoesNotExist:
                return HttpResponse("Invalid department ID.")

            try:
                role = Role.objects.get(id=role_id)
            except Role.DoesNotExist:
                return HttpResponse("Invalid role ID.")

            # Validate phone number (ensure it's numeric and has a reasonable length)
            if not phone.isdigit() or len(phone) < 10 or len(phone) > 15:
                return HttpResponse("Invalid phone number.")

            # Save the employee to the database
            new_emp = Employee(
                first_name=first_name,
                last_name=last_name,
                salary=salary,
                bonus=bonus,
                phone=phone,
                dept=dept,
                role=role
            )
            new_emp.save()
            return HttpResponse('Employee added successfully')

        except Exception as e:
            return HttpResponse(f"An error occurred: {e}")

    elif request.method == 'GET':
        departments = Department.objects.all()
        roles = Role.objects.all()
        return render(request, 'add_emp.html', {'departments': departments, 'roles': roles})
    else:
        return HttpResponse("An unexpected error occurred while adding the employee.")

def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee removed successfully")
        except Employee.DoesNotExist:
            return HttpResponse("Please enter a valid employee ID")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove_emp.html', context)

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()  # Fixed variable handling
        dept = request.POST.get('dept', '').strip()
        role = request.POST.get('role', '').strip()
        
        emps = Employee.objects.all()

        # Apply filters only if fields are provided
        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name__icontains=dept)
        if role:
            emps = emps.filter(role__name__icontains=role)

        context = {
            'emps': emps
        }
        return render(request, 'view_all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An exceptional error occurred while filtering employees.')
