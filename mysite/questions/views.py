from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic import TemplateView
from .models import Question, Tag, User, Answer, LikeQuestion, LikeAnswer
from .otherfuncs import paginate
from .otherfuncs import randomQuerySet
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def log_in(request):
    if (request.user.is_authenticated):
        return HttpResponseRedirect('home')
    if ( request.method == "POST" ):
        usern = request.POST.get('LoginInput','')
        passw = request.POST.get('inputPassword','')
        user = auth.authenticate(username=usern, password = passw)
        if (user is not None):
            auth.login(request,user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request,'login.html')
    return render(request,'login.html')

def likequestion(request, id):
    question_ = Question.objects.get(id = id)
    likeset = question_.likequestion_set.all()
    for l in likeset:
        if (l.user == request.user):
            l.delete()
            question_.likes = question_.likequestion_set.count()
            question_.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    ql = LikeQuestion(user=request.user, question=question_)
    ql.save()
    question_.likequestion_set.add(ql)
    question_.likes = question_.likequestion_set.count()
    question_.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def likeanswer(request, id):
    answer_ = Answer.objects.get(id = id)
    likeset = answer_.likeanswer_set.all()
    for l in likeset:
        if (l.user == request.user):
            l.delete()
            answer_.likes = answer_.likeanswer_set.count()
            answer_.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    al = LikeAnswer(user=request.user, answer=answer_)
    al.save()
    answer_.likes = answer_.likeanswer_set.count()
    answer_.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def question(request, id):
    question_ = get_object_or_404(Question,pk=id)
    answers = question_.answer_set.all()
    tags = randomQuerySet(Tag.objects.all(),5)
    users = User.objects.all()
    return render(request,'question.html', {'question': question_, 'tags':tags, 'users':users, 'answers':answers})

def hot(request):
    q = Question.objects.bylikes()
    tags = randomQuerySet(Tag.objects.all(), 5)
    users = User.objects.all()
    questions = paginate(q, request)
    return render(request, 'index.html',
                  {'questions': questions, 'tags': tags, 'users': users, 'page_title': "Questions"})

def base(request, sort = Question.objects.new()):
    q = sort
    tags = randomQuerySet(Tag.objects.all(),5)
    users = User.objects.all()
    questions = paginate(q,request)
    return render(request,'index.html',{'questions':questions, 'tags':tags, 'users':users, 'page_title':"Questions"})

def questions_on_tag(request,tag):
    q_o_t = Question.objects.filter(tags__title = tag)
    questions = paginate(q_o_t, request)
    tags = randomQuerySet(Tag.objects.all(),5)
    users = User.objects.all()
    return render(request, 'index.html',{'questions':questions,'tags':tags,'users':users, 'page_title':"On tag "+tag })

def ask_question(request):
    tags = randomQuerySet(Tag.objects.all(), 5)
    users = User.objects.all()
    return render(request, 'ask.html', {'tags':tags,'users':users, 'page_title':'Ask Question'})

@login_required
def log_out(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))

def registration(request):
    tags = randomQuerySet(Tag.objects.all(), 5)
    users = User.objects.all()
    return render(request, 'registration.html', {'tags':tags,'users':users, 'page_title':'Registration'})