from django.contrib import admin
from .models import Question, Answer

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['content']

admin.site.register(Question, QuestionAdmin)   # admin 관리자에 Question 모델을 등록하면, 장고 관리자 화면에서 Question을 관리할 수 있다
admin.site.register(Answer, AnswerAdmin)