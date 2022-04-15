from django.shortcuts import render

# Create your views here.
from .models import Quiz


def index(request):
    return render(request, 'index.html')


def quiz(request):
    questions = Quiz.objects.all()

    return render(request, 'quiz.html', {'questions': questions})


def admin(request):
    return render(request, 'admin.html')
