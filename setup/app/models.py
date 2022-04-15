from django.db import models


# Create your models here.
class Quiz(models.Model):
    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.question

    def __repr__(self):
        return f'Quiz(question={self.question}, option1={self.option1}, option2={self.option2}, option3={self.option3}, option4={self.option4}, answer={self.answer})'



