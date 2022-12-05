from django.urls import path
from .views import index
from .views import add_student, edit_student, student_list

urlpatterns = [
    path('', index, name='index'),
    path('add_student/', add_student, name='add_student'),
    path('all_student/', student_list, name='all_student'),
]
