from django.urls import path
from .views import result

urlpatterns = [
    path('list/', result, name='result'),
    path('transcript/', result, name='transcript')

]
