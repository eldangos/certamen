from django.shortcuts import render, HttpResponse

def home(request):
    return render(request,"core/home.html")

def foro(request):
    return render(request,"core/foro.html")
    
def quest(request):
    return render(request, "core/quest.html")

def gallery(request):
    return render(request, "core/gallery.html")


"""
def home(request):
    return HttpResponse("<h1>Inicio<h1/>")

def foro(request):
    return HttpResponse("<h1>Foro<h1/>")
"""