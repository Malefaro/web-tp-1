from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic import TemplateView
from .models import Question, Tag, User, Answer
from .models import paginate
# Create your views here.

def log_in(request):
    return render(request,'login.html')

def question(request, id):
    question_ = get_object_or_404(Question,pk=id)
    answers = question_.answer_set.all()
    tags = Tag.objects.all()
    users = User.objects.all()
    return render(request,'question.html', {'question': question_, 'tags':tags, 'users':users, 'answers':answers})

def base(request):
    q = Question.objects.new()
    tags = Tag.objects.all()
    users = User.objects.all()
    questions = paginate(q,request)
    return render(request,'index.html',{'questions':questions, 'tags':tags, 'users':users })