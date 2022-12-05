from django.db import models

# Create your models here.
class Result(models.Model):
    name = models.CharField(max_length = 200)
    def __str__(self):
        return self.name
    tcr = models.IntegerField()
    tce = models.IntegerField()
    gpa = models.FloatField()
    cgpa = models.FloatField()