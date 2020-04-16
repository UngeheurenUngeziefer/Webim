from django.shortcuts import render
from django.views.generic.base import View

from squares.models import Square

def squares(request):
    return render(request, 'squares/squares.html')

def jspage(request):
    return render(request, 'squares/js_page.html', {'values': ['pic1']})
