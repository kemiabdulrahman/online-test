from django.db import models
from django.contrib.auth.models import User
from quiz.models import Quiz


class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    class Meta:
        verbose_name = "Result"
        verbose_name_plural = "Results"

    def __str__(self):
        return str(self.pk) 

