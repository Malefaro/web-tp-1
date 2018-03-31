from django.conf.urls import url, re_path
from django.urls import path, include
from questions import views
from django.views.static import serve

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url('^$', views.base, name='home'),
    url('question/id(?P<id>\d+)/?$', views.question, name= 'question'),
    url('^login/', views.log_in,name = 'login'),
    #url(r'^upload/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)