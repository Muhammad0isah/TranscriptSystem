from django.db import models


# Create your models here.
class Course(models.Model):
    course_code = models.CharField(max_length=10)
    def __str__(self):
        return self.course_title
    course_title = models.CharField(max_length=50)
