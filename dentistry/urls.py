from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('doctors/', views.doctor_list, name='doctor_list'),
  path('doctors/<int:id>/', views.doctor_details, name='doctor_details'),
  path('schedule/', views.schedule, name='schedule'),
  path('appointments/<int:id>/', views.appointment_details, name='appointment_details'),
  path('patients/<int:id>/', views.patient_details, name='patient_details'),
]