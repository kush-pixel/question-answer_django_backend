from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Question(models.Model):
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False)
    # model_answer = models.TextFiel)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # def get_responses(self):
    #     return self.responses.filter(parent=None)


class Response(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    question = models.ForeignKey(
        Question, null=False, on_delete=models.CASCADE, related_name='responses')
    # parent = models.ForeignKey(
    #     'self', blank=True, on_delete=models.CASCADE)
    body = models.TextField(null=False)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body

    # def get_responses(self):
    #     return Response.objects.filter(parent=self)
# Created,updated and login, register URL should be removed and parent part should be removed.
