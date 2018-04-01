from django.contrib import admin

# Register your models here.

from questions.models import Question, User, Tag, Answer, LikeQuestion, LikeAnswer

admin.site.register(Question)
admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Answer)
admin.site.register(LikeQuestion)
admin.site.register(LikeAnswer)