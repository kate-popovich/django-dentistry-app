from django.shortcuts import render, get_object_or_404
from .models import Doctor, Appointment, Patient
import sys

# Create your views here.

def index(request):
  return render(request, 'index.html', {})

def doctor_list(request):
  doctor_list = list(Doctor.objects.all().values())
  return render(request, 'doctor_list.html', {'doctor_list':doctor_list})

def doctor_details(request, id):
  doctor = get_object_or_404(Doctor, id=id)
  patients = Patient.objects.all()
  all_appointments = Appointment.objects.all()
  doctor_appointments =[ap for ap in all_appointments if ap.doctor_id == doctor.id]

  appointments_with_patient_name = []

  for ap in doctor_appointments:
    patient = patients.filter(id=ap.patient_id).first()

    patient_name = f"{patient.first_name} {patient.last_name}"

    appointments_with_patient_name.append({
      'appointment': ap,
      'patient_name': patient_name,
      'appointment_datetime': ap.appointment_datetime,
    })

  context = {
    'doctor': doctor,
    'appointments': appointments_with_patient_name,
  }

  return render(request, 'doctor_details.html', context)

def schedule(request):
  appointments = Appointment.objects.all()
  patients = Patient.objects.all()

  appointments_with_patient_name = []

  for ap in appointments:
    patient = patients.filter(id=ap.patient_id).first()

    patient_name = f"{patient.first_name} {patient.last_name}"

    appointments_with_patient_name.append({
      'appointment': ap,
      'patient_name': patient_name,
      'appointment_datetime': ap.appointment_datetime,
    })

  context = {
    'appointments': appointments_with_patient_name,
  }

  return render(request, 'schedule.html', context)