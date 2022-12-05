from django import forms
from .models import Student
from django.forms import NumberInput, TextInput


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'student_id',
                  'gender', 'date_of_birth', 'faculty', 'department',
                  'level', 'admission_number', 'phone_number',
                  ]
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'student_id': NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'id': 'gender_list', 'class': 'form-control'}),
            'date_of_birth': NumberInput(attrs={'class': 'form-control', 'type': 'date'}),
            'faculty': TextInput(attrs={'class': 'form-control'}),
            'department': TextInput(attrs={'class': 'form-control'}),
            'level': forms.Select(attrs={'id': 'level_list', 'class': 'form-control'}),
            'admission_number': TextInput(attrs={'class': 'form-control'}),
            'phone_number': TextInput(attrs={'class': 'form-control'}),

        }
