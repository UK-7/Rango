from django.shortcuts import render
from django.http import HttpResponse

# Home page

def index(request):
      return HttpResponse("Rango says hey there world! <br/> <a href='/rango/about'>About</a>")


# About page

def about(request):
      return HttpResponse("Rango says this is the about page!<a href='/rango/'>Index</a>")
