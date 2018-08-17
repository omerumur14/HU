from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def home(request):
        return render(request, "home.html", {})
