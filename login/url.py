from django.urls import path
from .views import welcome, login, register

urlpatterns = [
    path('', welcome, name='welcome'),
    path('login/', login, name='login'),
    path('register/', register, name='register')
]
