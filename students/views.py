from django.shortcuts import render , redirect, get_object_or_404
from  .models import Student
from .forms import StudentForm , UserRegistrationForm , UserLoginForm
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from django.contrib.auth import  login, authenticate,logout
from rest_framework.views import APIView
from .serializers import StudentSerializer
from rest_framework.response import Response
# Create your views here.

@login_required
def student_list(request):
    students=Student.objects.all()
    return render(request,'students/student_list.html',{'students':students})

@login_required
def student_create(request):
    form=StudentForm(request.POST )
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request,'students/student_form.html',{'form':form})

@login_required
def student_update(request , id):
    student= get_object_or_404(Student, id=id)
    form=StudentForm(request.POST , instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request,'students/student_form.html',{'form':form})

@login_required
def student_delete(request , id):
    student= get_object_or_404(Student, id=id)
    if request.method=="POST":
        student.delete()
        return redirect('student_list')
    return render(request,'students/student_confirm_delete.html',{'student':student})


def register(request):
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} ! You can now log in .')
            return redirect('login')
    else:
            form=UserRegistrationForm()
    return render(request, 'students/register.html', {'form':form})


def dashboard(request):
    total_students= Student.objects.count()
    return render (request, 'students/dashboard.html',{'total_students':total_students})

def LoginView(request):
    if request.method=="POST":
        form=UserLoginForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
            return redirect('student_list')
    else:
         form=UserLoginForm()
    return render(request,'students/login.html',{'form':form})
    
def logoutView(request):
    logout(request)
    return redirect('dashboard')

class StudentAPI(APIView):
    def get (self, request):
      students=Student.objects.all()  
      serializer=StudentSerializer (students, many=True)  
      return Response(serializer.data)
