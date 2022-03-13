import json
import os
import random
from collections import namedtuple

question_data = namedtuple('question_data', 'question, answers, answer_key')


class QuizApp(object):
    def __init__(self, fileName=None):
        self.chapter = ""
        self.title = ""
        self.no = ""

        self.Data = None

        # check for file name
        if fileName != None:
            self.load_data(fileName)

        # print(f"{self.chapter} - {self.title} - {self.no}")

    def load_data(self, fileName):
        # open file which already defined on path
        with open(fileName, 'r') as file_to_load:
            data_file = json.load(file_to_load)
            '''
            begin parse json data which already defined
            '''
            self.chapter = data_file['chapter']
            self.title = data_file['title']
            self.no = data_file['no']

            # data = data_file['data']

            # print(type(data))
            # print(f"size: {len(data)} - {data[0]['answers'][0]}")
            #
            # for data_item in data:
            #     self.question_data.append(data_item['question'])
            #     print(f"{self.question_data}\n{type(data_item['answers'])}")

            self.Data = [question_data(**ind) for ind in data_file['data']]

            # print(f"{self.Data}\nover all data: {len(self.Data)}\n{len(self.Data[0].answers)}")
            # print(f"chapter: {self.chapter}, title: {self.title}, no: {self.no}")

            # print(random.sample(self.Data, 1))

    def start(self, num_question_to_display):
        '''
        begin the quiz
        question gonna be in random pick
        '''

        print(f"Evaluasi {self.title} - {self.chapter} ke {self.no}")
        input("Tekan {ENTER} apabila Anda sudah siap >>>")

        random_data = random.sample(self.Data, num_question_to_display)

        for i in range(len(random_data)):
            print(f"[Soal: {i + 1}]")
            print(f"{random_data[i].question}")


# https://stackoverflow.com/questions/9271464/what-does-the-file-variable-mean-do
QuizApp(os.path.dirname(__file__) + '/question.json').start(3)
