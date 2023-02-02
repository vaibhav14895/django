from django.shortcuts import render, HttpResponse
from app.models import forms
from .forms import input


def form(request):
    bdata = forms.objects.all()
    data = {
        'data': bdata
    }
    return render(request, "form.html", data)


def create(request):
    form = input()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponse("thankyou")
        else:
            form = input()
    return render(request, 'create.html', {'form': form})


def home(request):
    return render(request, "home.html")
