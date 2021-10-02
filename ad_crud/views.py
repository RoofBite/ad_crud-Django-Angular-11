from django.shortcuts import render
from django.urls import reverse

def index(request):
    return render(request, "ad_crud/index.html")
