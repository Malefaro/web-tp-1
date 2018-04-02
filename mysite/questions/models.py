from django.db import models

# Create your models here.
from django.conf import settings
import os
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-create_date')
    def bylikes(self):
        return self.order_by('-likes')


class User(AbstractUser):
    email = models.EmailField(unique=True)
    upload = models.ImageField(default='user.png',upload_to='uploads/%Y/%m/%d')


class Tag(models.Model):
    title = models.CharField(max_length=120, verbose_name=u"Заголовок ярлыка")

    def __str__(self):
        return self.title

class Question(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u"Автор")
    title = models.CharField(max_length=120, verbose_name=u"Заголовок вопроса")
    text = models.TextField(verbose_name=u"Полное описание вопроса")
    create_date = models.DateTimeField(default=datetime.now, verbose_name=u"Время создания вопроса")
    is_active = models.BooleanField(default=True, verbose_name=u"Доступность вопроса")
    tags = models.ManyToManyField(Tag, blank=True)
    objects = QuestionManager()
    likes = models.IntegerField(default=0, verbose_name=u"Лайки")
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_date']

class LikeQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u"Пользователь")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name=u'Вопрос')

    def __str__(self):
        return self.user.username + " like Q: " + str(self.question)
    # def like(self,request):
    #     likeset = self.question.likequestion_set.all()
    #     for l in likeset:
    #         if (l.user == request.user):
    #             return


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u"Пользователь")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name=u'Вопрос')
    text = models.TextField(verbose_name=u"Ответ")
    create_date = models.DateTimeField(default=datetime.now, verbose_name=u"Время ответа")
    id = models.IntegerField(unique=True, primary_key=True)
    is_correct = models.BooleanField(default=False, verbose_name=u'Корректность')
    likes = models.IntegerField(default=0, verbose_name=u"Лайки")

    def __str__(self):
        return "Q: " + self.question.title + " User:" + self.user.username

    class Meta:
        ordering = ['-create_date']

class LikeAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u"Пользователь")
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, verbose_name=u'Вопрос')

    def __str__(self):
        return self.user.username + " like on " + str(self.answer)