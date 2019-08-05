from django.shortcuts import render, HttpResponse

# Create your views here.
html_base = """

<h1>My personal web</h1>

<ul>
    <li><a href="/">Home</a></li>
    <li><a href="/about-me">About me</a></li>
    <li><a href="/portafolio">Portafolio</a></li>
    <li><a href="/contact">Contact</a></li>

"""


def home(request):

    return HttpResponse(html_base+"""
    <h2>Cover</h2>
    <p>This is a cover baby</p>
    """)


def about(request):
    return HttpResponse(html_base+"""
    <h2>About me</h2>
    <p>Hello friend, my name is Andrea Fuentes and I'm software developer.</p>
    """)


def portafolio(request):

    return HttpResponse(html_base+"""
    <h2>Portafolio</h2>About me
    <p>This is a portafolio :)</p>
    """)


def contact(request):
    return HttpResponse(html_base+"""
    <h2>Contact</h2>
    <p>My contact is: AFU92</p>
    """)
