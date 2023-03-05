from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=30)
    hours = models.DurationField()
    price = models.FloatField()

class Mentor(models.Model):
    surname = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=25, null=True)
    photo = models.ImageField()
    date_of_birth = models.DateTimeField()
    QualificationType = models.TextChoices('QualificationType', 'Junior Middle Senior')
    qualification = models.CharField(blank=True, choices=QualificationType.choices, max_length=10)
    add_info = models.Model(max_length=40)



class Listener(models.Model):
    surname = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=25, null=True)
    photo = models.ImageField()
    date_of_birth = models.DateTimeField()
    email = models.EmailField()
    phone_number = models.PositiveIntegerField()
    passed_courses = models.ManyToManyField(Course)

class Request(models.Model):
    listener = models.ManyToManyField(Listener)
    course = models.ManyToManyField(Course)
    DaysofstudyType = models.TextChoices('DaysofstudyType', 'Monday Tuesday Wednesday Thursday Friday Saturday')
    days_of_study = models.CharField(blank=True, choices=DaysofstudyType.choices, max_length=60)
    time_of_study = models.TimeField()

class Group(models.Model):
    course = models.ManyToManyField(Course)
    mentor = models.ManyToManyField(Mentor)
    listener = models.ManyToManyField(Listener)
    launch_time = models.TimeField()
    days_of_study = models.CharField(blank=True, choices=DaysofstudyType.choices, max_length=60)
