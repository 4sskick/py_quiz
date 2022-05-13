import json
import os
import random
from collections import namedtuple

from django.shortcuts import render

# Create your views here.
from .models import Quiz


def __load_questions():
    question_data = namedtuple('question_data', 'question, answers, answer_key')
    with open(os.path.dirname(__file__)+'/data/question.json', 'r') as file:
        quiz_json = json.load(file)

        questions = [question_data(**ind) for ind in quiz_json['data']]

    return questions


def index(request):
    return render(request, 'index.html')


def quiz(request):
    # querying data model which already filled by data
    questions = Quiz.objects.all()

    # would randomize data questions
    num_question = [1, 2]
    random_data = random.sample(list(questions), len(num_question))
    q_data = zip(random_data, num_question)

    return render(request, 'quiz.html', {'questions': q_data})


def admin(request):
    # questions = Quiz.objects.all()
    questions = __load_questions()

    dict = {
        'questions': questions,
        'type_of': type(questions)
    }

    return render(request, 'admin.html', dict)
