from django.shortcuts import render
from django.http import HttpResponse

# Home page

def index(request):
      context_dict = {'boldmessage': "I am bold font from the context"}
      return render(request, 'rango/index.html', context_dict)


# About page

def about(request):
      return HttpResponse("Rango says this is the about page!<a href='/rango/'>Index</a>")
