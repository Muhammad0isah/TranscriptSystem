from django.urls import path
from .views import course, course_add

urlpatterns = [
    path('course/', course, name='course'),
    path('add_course/', course_add, name='add_course')
]
