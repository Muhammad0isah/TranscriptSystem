from django.shortcuts import render, redirect
from .form import StudentForm
from .models import Student

# Create your views here.
def index(request):
    return render(request, 'index.html')


def add_student(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('student/')

    context = {'form': form}
    return render(request, 'add-student.html', context)


def edit_student(request):
    return render(request, 'edit-student.html')


def student_list(request):
    all_student = Student.objects.all()
    context = {'student':all_student}
    return render(request, 'students.html',context)

