from django.shortcuts import render, redirect
from .models import Course
from .form import CourseForm


# Create your views here.
def course_add(request):
    course_form = CourseForm()
    if request.method == 'POST':
        course_form = CourseForm(request.POST)
        if course_form.is_valid():
            course_form.save()
            return redirect('add_course')
    context = {'form': course_form}
    return render(request, 'add-subject.html', context)


def course(request):
    model_course = Course.objects.all()
    context = {'course': model_course}
    return render(request, 'subjects.html', context)
