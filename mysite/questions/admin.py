from django.contrib import admin

# Register your models here.

from questions.models import Question

admin.site.register(Question)
