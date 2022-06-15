import json
import os
import random
from collections import namedtuple

from django.shortcuts import render

# Create your views here.
from .models import Quiz


def __getAnswerByIndex(j, item):
    return {
        "content": item['answers'][j],
        "is_answer": int(j == item['answer_key'])
    }


def __load_questions():
    question_data = namedtuple('question_data', 'question, answers, answer_key')
    questions = []

    with open(os.path.dirname(__file__) + '/data/question.json', 'r') as file:
        quiz_json = json.load(file)

        # questions = [question_data(**ind) for ind in quiz_json['data']]

        for i in range(len(quiz_json)):
            item = quiz_json['data'][i]

            answerKey = list(map(
                # __getAnswerByIndex(_, item['answers'])

                # function to handle iterable
                lambda index_iterable: {
                    "content": item['answers'][index_iterable],
                    "is_answer": int(index_iterable == item['answer_key'])
                }

                # loop iterate from index 0 ... length of item['answers]
                , range(len(item['answers']))
            ))

            questions.append({
                "detail_no": quiz_json['no'],
                "detail_chapter": quiz_json['chapter'],
                "detail_title": quiz_json['title'],
                "question": item['question'],
                "readable_answer_key": answerKey
            })

    return questions


def __enumarate(arrData):
    for i in range(len(arrData)):
        arrData[i]['no'] = i + 1

    return arrData


def index(request):
    return render(request, 'index.html')


def serve_evaluation(request):
    # querying data model which already filled by data
    # questions = Quiz.objects.all()
    questions = __load_questions()

    # would randomize data questions

    questions = random.sample(list(questions), 2)
    for item in questions:
        random.shuffle(item['readable_answer_key'])
        item['readable_answer_key'] = __enumarate(item['readable_answer_key'])

    random.shuffle(questions)
    questions = __enumarate(questions)

    data = {
        'questions': questions
    }

    return render(request, 'quiz.html', data)


def serve_admin(request):
    # questions = Quiz.objects.all()
    questions = __load_questions()

    data = {
        'questions': questions,
        'type_of': type(questions)
    }

    return render(request, 'admin.html', data)
