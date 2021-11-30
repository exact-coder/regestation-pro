from django.db import models

# Create your models here.

class Student(models.Model):
    department_choices = (
        ('Engineering','Engineering'),
        ('Agriculture','Agriculture'),
        ('Accounting','Accounting'),
        ('Tresurer','Tresurer'),
        ('MPDC','MPDC'),
        ('MCTC','MCTC'),
        ('MCR','MCR'),
        ('Mayor','Mayor'),
        ('Tourism','Tourism'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.CharField(choices=department_choices,max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact_no = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.username

