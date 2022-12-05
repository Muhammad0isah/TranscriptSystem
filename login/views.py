from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .form import RegisterForm, LoginForm


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')


def login(request):
    user = LoginForm(request.POST)
    context = {'login': user}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, "incorrect username or password")
            return redirect('login')
    else:
        return render(request, 'login.html', context)


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if form.is_valid():
            form.save()
            if password == confirm_password:
                if User.objects.filter(email=email).exists():
                    messages.info(request, "email already exist")
                    redirect('register')
                elif User.objects.filter(username=username).exists():
                    messages.info(request, 'username already exits')
                    redirect('register')
                else:
                    form = User.objects.create_user(username=username, email=email, password=password)
                    form.save()
                    redirect('login')
            else:
                messages.info(request, "incorrect password")
                return redirect('register')
    context = {'register': form}

    return render(request, 'register.html',context)
