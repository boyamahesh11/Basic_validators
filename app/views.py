from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.

def student(request):
    sfo=StudentForm()
    d={'sfo':sfo}
    if request.method=="POST":
        sfd=StudentForm(request.POST)
        if sfd.is_valid():
            return HttpResponse(str(sfd.cleaned_data))
        else:
            return HttpResponse('data is not valid')

    return render(request,'student.html',d)
