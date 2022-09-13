from unicodedata import name
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def enviar(request):
    user = request.POST['user']
    passw = request.POST['pass']

    if (user=='huamani' and passw =='123'):
        context={
        'nombre':user,
        'clave':passw,
        }
        return render(request,'respuesta.html',context)
    context={
        'nombre':user,
        'clave':passw,
        }
    return render(request,'nologin.html',context)

def calcular(request):
    hours = int(request.POST['hours'])
    payment = int(request.POST['payment'])
    context={
        'nombre':hours,
        'clave':payment,
    }
    if hours <= 48 and hours>0:
        total = hours * payment
        context={
            'total':total
        }
        return render(request,'pagoresultado.html',context)
    if hours > 48:
        total = 2 * hours * payment
        context={
            'total':total
        }
        return render(request,'pagoresultado.html',context)
    return render(request,'datosinvalidos.html',context)