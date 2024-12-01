from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('doctors/', views.doctor_list, name='doctor_list'),
  path('doctors/<int:id>/', views.doctor_details, name='doctor_detail'),
  path('schedule/', views.schedule, name='schedule'),
]