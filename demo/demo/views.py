from django.shortcuts import render
from django.http import HttpResponse
from . import urls

def index(request):
    return render(request,'index.html', {
        'message': 'Listado de productos',
        'window': 'Productos',
        'products': [
            {'title': 'Playera', 'price':5, 'stock': True},
            {'title': 'Camisa', 'price':7, 'stock': True},
            {'title': 'Mochila', 'price':20, 'stock': False},
        ]
        })