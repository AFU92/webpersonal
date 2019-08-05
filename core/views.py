from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):

    return HttpResponse("<h1>My personal web</h1><h2>Cover</h2>")


def about(request):
    return HttpResponse("<h1>My personal web</h1><h2>About</h2><p>Hello, my name is andrea</p>")
