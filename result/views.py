from django.shortcuts import render
from .models import Result

# Create your views here.
def result(request):
    all_result = Result.objects.all()
    context = {'all_result':all_result}
    return render(request, 'result.html',context)
