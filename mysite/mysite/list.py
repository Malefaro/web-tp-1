from questions.models import Question
from django.views.generic import ListView
from django.http import Http404
from django.shortcuts import render, get_object_or_404

class QuestionList(ListView):
    model = Question
    paginate_by = 1

def question_detail(requst, question_id):
    try:
        r_d = {
            'question': Question.objects.get(pk=question_id)
        }
    except Question.DoesNotExist as e:
        raise Http404
    return render(requst, 'question_detail.html', r_d)
#Это эквивалентно тому что ты написал в тетради