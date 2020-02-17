from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def blog(request):
    return render(request, 'blog.html', {})   

 
def recetas(request):
    return render(request, 'recetas.html', {}) 

def contacto(request):
    return render(request, 'contacto.html', {})    