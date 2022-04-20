from msilib.schema import ListView
from django.shortcuts import render
from .models import Game

def home(request):
    qs = Game.objects.all()
    context = {'objects_list': qs}
    return render(request, 'games/home.html', context)