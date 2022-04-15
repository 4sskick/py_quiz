import random

from django.shortcuts import render

# Create your views here.
from .models import Quiz


def index(request):
    return render(request, 'index.html')


def quiz(request):
    questions = Quiz.objects.all()

    # would randomize data questions
    num_question = [1, 2]
    random_data = random.sample(list(questions), len(num_question))
    q_data = zip(random_data, num_question)

    return render(request, 'quiz.html', {'questions': q_data})


def admin(request):
    questions = Quiz.objects.all()

    return render(request, 'admin.html', {'questions': questions})
