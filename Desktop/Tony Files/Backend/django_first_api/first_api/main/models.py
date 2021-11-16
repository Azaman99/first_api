from datetime import datetime
from django.db import models
from django.utils import timezone




# Create your models here.
def my_cohort():
    ## Function to get cohort's month and year of registration
    date = timezone.now()
    cohort = datetime.strftime(date, "%B-%Y")
    return cohort
    

class Student(models.Model):
    name = models.CharField(max_length=50)
    cohort = models.CharField(max_length = 100, default = my_cohort())
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    @property
    def book(self):
        return self.books.all().values()
    


class Book(models.Model):
    title = models.CharField(max_length=200)
    student = models.ForeignKey("Student", on_delete=models.CASCADE, related_name = "books")
    author =  models.CharField(max_length=100)
    num_of_pages = models.IntegerField(default=50)


    def __str__(self):
        return self.title


    @property
    def student_name(self):
        return self.student.name