from django.db import models
from datetime import datetime, date, time
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Date:
    def __init__(self, year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def daymonthyear(cls, day, month, year):
        cls.year = year
        cls.month = month
        cls.day = day


class Contact(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=15, unique=True)
    enquiry_reason = models.TextField(max_length=1600)
    sent_on = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    date_of_event = models.DateField()
    time_of_event = models.TimeField()
    title_of_event = models.CharField(max_length=150)
    event_content = models.CharField(max_length=200)
    event_photo = models.ImageField(
        null=True, blank=True, upload_to="eventsimages/")

    def __str__(self):
        return self.title_of_event

# Model to add event picker ID's


class Eventpicker(models.Model):
    picker = models.CharField(
        max_length=6, blank=True, null=True)
    picker_eid = models.IntegerField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.picker


class Classes(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name


# class Admission(models.Model):
#     fname_of_student = models.CharField(max_length=100)
#     mname_of_student = models.CharField(max_length=100, blank=True)
#     lname_of_student = models.CharField(max_length=100)
#     dob = models.DateField(blank=True)
#     # address_of_student = models.CharField(max_length=600, blank=True)
#     class_of_interest = models.ForeignKey(Classes, on_delete=models.CASCADE)
#     parents_name = models.CharField(max_length=100)
#     parents_phone = models.CharField(max_length=15)
#     parents_email = models.EmailField(max_length=150, blank=True)
#     parents_address = models.CharField(max_length=600, blank=True)
#     submitted_on = models.DateField(auto_now_add=True, blank=True)


#     def __str__(self):
#         return self.fname_of_student

class Admission(models.Model):
    SELECT_GENDER = [('Female', 'Female'), ('Male', 'Male')]
    CLAS_CHOICE = [("PLAYGROUP", "Playgroup"), ("PRENURSERY", "Prenursery"), ("NURSERY1", "Nursery1"), ("NURSERY2", "Nursery 2"), 
                   ("PRIMARY1", "Primary 1"), ("PRIMARY2", "Primary 2"), ("PRIMARY3","Primary 3"), ("PRIMARY4", "Primary 4"), 
                   ("PRIMARY5", "Primary 5"), ("PRIMARY6","Primary 6"), ("SUMMER", "Summer")]
    first_name = models.CharField(verbose_name="Student's First Name", max_length=100, help_text="Input the Student's First Name")
    middle_name = models.CharField(verbose_name="Student's Second Name", max_length=100, help_text="Input the Student's Second Name")
    last_name = models.CharField(verbose_name="Student's Surname Name", max_length=100, help_text="Input the Student's Surname Name")
    gender = models.CharField(max_length=6, choices=SELECT_GENDER)
    date_of_birth = models.DateField(null=True, blank=True)
    clas_of_admission = models.CharField(verbose_name='Class Of Admission', choices=CLAS_CHOICE, max_length=15)
    parent_name = models.CharField(verbose_name="Parent's Name", max_length=200, help_text="Enter the name of parent")
    parent_phone_number = PhoneNumberField(verbose_name="Parent's Phone Number", region='NG', max_length=14)
    parent_email = models.EmailField(verbose_name="Email Address", help_text="Provide Valide Email Address")
    address = models.CharField(verbose_name="Residential Address", max_length=200)
    date_created = models.DateField(verbose_name="", auto_now=True)