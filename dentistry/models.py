from django.db import models

class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    snils = models.CharField(max_length=11, unique=True)  # СНИЛС
    inn = models.CharField(max_length=12, unique=True)    # ИНН

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"


class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    allergies_info = models.TextField(blank=True)
    discount_info = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_datetime = models.DateTimeField()

    def __str__(self):
        return f"Приём {self.doctor} - {self.patient} на {self.appointment_datetime}"


class Procedure(models.Model):
    appointment = models.ForeignKey(Appointment, related_name='procedures', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.title} - {self.cost} руб."
