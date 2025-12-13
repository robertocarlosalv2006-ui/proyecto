from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def paginabienvenida(request):
    titulo= "yo soy Roberto Alvia soy autista"

    return render(request, 'signup.html',{'mytitle':titulo})
