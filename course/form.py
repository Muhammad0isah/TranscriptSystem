from django import forms
from django.forms import TextInput

from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_code', 'course_title']
        widgets = {
            'course_code': TextInput(attrs={'class': 'form-control'}),
            'course_title': TextInput(attrs={'class': 'form-control'}),
        }
