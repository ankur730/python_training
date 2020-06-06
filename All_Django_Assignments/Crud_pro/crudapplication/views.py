from django.shortcuts import render, redirect
from crudapplication.models import Employee
from crudapplication.forms import EmployeeForm


# Create your views here.

def index(request):
    return render(request, 'crudapplication/index.html')

def create_view(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'crudapplication/create.html', {'form':form})

def retrieve(request):
    employees = Employee.objects.all()
    return render(request, 'crudapplication/retrieve.html', {'employees':employees})

def delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/retrieve')

def update(request, id):
    employee = Employee.objects.get(id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'crudapplication/update.html', {'employee':employee})
