from django.db import models

# Create your models here.

class Doctor (models.Model):
  surname = models.CharField(max_length=20, unique=False, help_text="Enter the surname")
  name = models.CharField(max_length=20, unique=False, help_text="Enter the name")
  middle_name = models.CharField(max_length=20, unique=False, help_text="Enter the middle name")
  birthday = models.DateField(unique=False, help_text="Enter your birthday")
  snils = models.IntegerField(unique=True, max_length=11, help_text="Enter your SNILS")
  inn = models.IntegerField(unique=True, max_length=12, help_text="Enter your INN")