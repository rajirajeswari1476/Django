from django.urls import path

from accounts import views

urlpatterns = [
path("",views.home_fun,name='home'),
   path('login',views.login_fun,name='login'),
   path('registration',views.registration,name='registration'),
   path('logout',views.user_logout,name='logout'),
path('employee_list',views.employee_list,name='employee_list'),
path('student_list',views.student_list,name='student_list'),
path('add_new_student',views.add_new_student,name='add_new_student'),
path('update/<int:id>',views.update_student,name='update'),
path('delete/<int:id>',views.delete_student,name='delete')
   ]

