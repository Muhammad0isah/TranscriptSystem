from django.db import models


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

    last_name = models.CharField(max_length=100)
    student_id = models.PositiveIntegerField()
    gender_list = (
        ('1', 'male'),
        ('2', 'female '),
    )
    gender = models.CharField(max_length=100, choices=gender_list)
    date_of_birth = models.DateField(auto_created='True')
    level_list = (
        ('1', 'level 100'),
        ('2', 'level 200'),
        ('3', 'level 300'),
        ('4', 'level 400'),
    )
    faculty = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    level = models.CharField(max_length=10, choices=level_list)
    admission_number = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=11)
