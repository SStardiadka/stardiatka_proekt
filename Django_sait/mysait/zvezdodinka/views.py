from django.shortcuts import render
from django.http import HttpResponse
from .models import Baza

def index(request):
    data ={
        'title': 'Продажа черенков и цветов на срезку!!!',
        'obj':{'Белые': 1,'Бронза': 2,'Желтые': 3}
    }
    return render(request, 'zvezdodinka/index.html', data)

def about(recuest):
    news = Baza.objects.order_by('-data')
    return render(recuest, 'zvezdodinka/about.html', {'news': news})

def regustr(recuest):
    return render(recuest, 'zvezdodinka/registr.html' )

# Create your views here.
