from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question


def index(request):     # pybo 목록 출력 (question_list)
    question_list = Question.objects.order_by('-create_date')   # 질문 목록 데이터를 가져와 order_by(조회결과정렬)하는 함수, -create_date는 역방향 정렬
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)  # 파이썬 데이터를 템플릿에 적용하여 HTML로 반환하는 함수

def detail(request, question_id):       # pybo 내용 출력 (question_detail)
    question = get_object_or_404(Question, pk=question_id)  # pk는 Question 모델의 기본키(Primary Key)인 id를 의미
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):     # pybo 답변 등록
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:detail', question_id=question.id)