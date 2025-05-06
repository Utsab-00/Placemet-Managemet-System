from django.urls import path
from . import views 
from .views import login_view
 # Import views from the same app

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.student_list, name='student_list'),
    path('companies/', views.company_list, name='company_list'),
    path('admins/', views.admin_list, name='admin_list'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]
