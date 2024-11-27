from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def fantasy_view(request):
    return render(request, 'fantasy.html')

def fiction_view(request):
    return render(request, 'fiction.html')

def action_adventure_view(request):
    return render(request, 'action_adventure.html')

def mistery_view(request):
    return render(request, 'mistery.html')

def horror_view(request):
    return render(request, 'horror.html')

def thriller_suspense_view(request):
    return render(request, 'thriller_suspense.html')

def romance_view(request):
    return render(request, 'romance.html')
