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


def student_list(request):
    students=Student.objects.all().order_by('id')
    return render(request,'students/student_list.html',{'students':students})

@login_required
def add_student(request):
    if request.method=='POST':
      form=StudentForm(request.POST )
      if form.is_valid():
         form.save()
         return redirect('student_list')
      else:
         print(form.errors)
    else:
        form=StudentForm()
    return render(request,'students/add_student.html',{'form':form})

@login_required
def edit_student(request, pk):
    student= get_object_or_404(Student, pk=pk)
    if request.method=='POST':
       form=StudentForm(request.POST , instance=student)
       if form.is_valid():
         form.save()
         return redirect('student_list')
       else:
        print(form.errors)
    else:
        form=StudentForm (instance=student)
    return render(request,'students/edit_student.html',{'student':student})

@login_required
def delete_student(request , pk):
    student= get_object_or_404(Student, pk=pk)
    if request.method=="POST":
        student.delete()
        return redirect('student_list')
    return render(request,'students/delete_student.html',{'student':student})


def register(request):
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ' Account created successfully! You can now log in .')
            return redirect('login')
        else:print("Form Validation Failed! Errors:",form.errors)
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
    messages.info(request, 'You have been logged out.')
    return redirect('login')

class StudentAPI(APIView):
    def get (self, request):
      students=Student.objects.all()  
      serializer=StudentSerializer (students, many=True)  
      return Response(serializer.data)

def home(request):
    return render (request, 'students/home.html ')

def base(request):
    return render(request, 'students/base.html')