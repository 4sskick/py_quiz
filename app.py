import json
import os


class QuizApp(object):
    def __init__(self, fileName=None):
        self.chapter = ""
        self.title = ""
        self.no = ""

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


# https://stackoverflow.com/questions/9271464/what-does-the-file-variable-mean-do
QuizApp(os.path.dirname(__file__) + '/question.json')
