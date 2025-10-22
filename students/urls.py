
from django .urls import path
from .import views as v
from  .views import StudentAPI

urlpatterns=[
    path('', v.student_list, name='student_list'),
    path('add/', v.student_create, name='student_create'),
    path('student_update/<int:id>/', v.student_update, name='student_update'),
    path('student_delete/<int:id>/', v.student_delete, name='student_delete'),
    path('login/', v.LoginView,name='login'),
    path('logout/', v.logoutView, name='logout'),
    path('register/', v.register, name='register'),
    path('dashboard/', v.dashboard, name='dashboard'),
    path('students/' , StudentAPI.as_view())
]
