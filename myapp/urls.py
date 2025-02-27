from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('employee_list/', views.employee_list_view, name='employee-list'),
    path('employee_create/', views.employee_create_view, name='employee-create'),
    path('employee_update/<int:pk>/', views.employee_update_view, name='employee-update'),
    path('employee_delete/<int:pk>/', views.employee_delete_view, name='employee-delete'),

]