
from django .urls import path
from .import views as v
from  .views import StudentAPI

urlpatterns=[
    path('', v.home, name='home'),
    path('students/', v.student_list, name='student_list'),
    path('students/add/', v.add_student, name='add_student'),
    path('students/edit/<int:pk>/', v.edit_student, name='edit_student'),
    path('students/delete/<int:pk>/', v.delete_student, name='delete_student'),
    path('login/', v.LoginView,name='login'),
    path('logout/', v.logoutView, name='logout'),
    path('register/', v.register, name='register'),
    path('dashboard/', v.dashboard, name='dashboard'),
    path('students/' , StudentAPI.as_view()),
    path('base/', v.base, name='base'),
    
]
