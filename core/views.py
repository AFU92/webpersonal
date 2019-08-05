from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    html_response = "<h1>My personal web</h1>"

    for i in range(10):
        html_response += f"<h2>Cover {i}</h2>"
    return HttpResponse(html_response)
