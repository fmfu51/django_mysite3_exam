from django.db import models

class Question(models.Model):
    subject = models.CharField(max_length=200)  # 글자 길이가 제한된 문자열은 CharField 타입 사용
    content = models.TextField()    # TextField는 제한이 없는 문자열에 사용
    create_date = models.DateTimeField()    # 날짜, 시간에 관계된 속성은 DateTimeField 사용

    def __str__(self):  # 모델을 조회할 때, id 값 대신 제목을 표시하는 함수
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # ForeignKey는 다른 모델과 연결하며, on_delete~ 는 이 답변과 연결된 질문이 삭제되면 함께 삭제된다는 뜻
    content = models.TextField()
    create_date = models.DateTimeField()

