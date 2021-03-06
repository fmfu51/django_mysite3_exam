from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')  # on_delete ~ : 계정이 삭제되면 작성한 질문도 모두 삭제됨
    subject = models.CharField(max_length=200)  # 글자 길이가 제한된 문자열은 CharField 타입 사용
    content = models.TextField()  # TextField는 제한이 없는 문자열에 사용
    create_date = models.DateTimeField()  # 날짜, 시간에 관계된 속성은 DateTimeField 사용
    modify_date = models.DateTimeField(null=True, blank=True)   # 질문 수정 일시(아래는 답변 수정 일시
    voter = models.ManyToManyField(User, related_name='voter_question')  # 추천인 추가

    def __str__(self):  # 모델을 조회할 때, id 값 대신 제목을 표시하는 함수
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # ForeignKey는 다른 모델과 연결하며, on_delete~ 는 이 답변과 연결된 질문이 삭제되면 함께 삭제된다는 뜻
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)  # null=True, blank=True는 어떤 조건으로든 값을 비워둘 수 있음
    voter = models.ManyToManyField(User, related_name='voter_answer')


class Comment(models.Model):    # 댓글 모델
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 글쓴이
    content = models.TextField()    # 내용
    create_date = models.DateTimeField()    # 작성 일시
    modify_date = models.DateTimeField(null=True, blank=True)   # 수정 일시
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE) # 이 댓글이 달린 질문
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)  # 이 댓글이 달린 답변