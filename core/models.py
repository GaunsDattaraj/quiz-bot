from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text

class UserResponse(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=255)  # Assuming user_id is a string, adjust as necessary
    response = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user_id} - {self.question.question_text}: {self.response}"
