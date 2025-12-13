from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def paginabienvenida(request):
    titulo= "jorge el Curioso"

    return render(request, 'signup.html',{'mytitle':titulo})
