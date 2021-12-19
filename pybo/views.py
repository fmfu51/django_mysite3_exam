from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import QuestionForm, AnswerForm
from .models import Question
from django.core.paginator import Paginator


def index(request):  # pybo 목록 출력 (question_list)
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지

    # 조회
    question_list = Question.objects.order_by('-create_date')

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)  # 파이썬 데이터를 템플릿에 적용하여 HTML로 반환하는 함수


def detail(request, question_id):  # pybo 내용 출력 (question_detail)
    question = get_object_or_404(Question, pk=question_id)  # pk는 Question 모델의 기본키(Primary Key)인 id를 의미
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)


def answer_create(request, question_id):  # pybo 답변 등록
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)


def question_create(request):  # pybo 질문 등록
    if request.method == 'POST':
        form = QuestionForm(request.POST)   # request.POST에는 화면에서 사용자가 입력한 내용들이 담겨있음
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save() # 입력한 질문데이터를 저장, 시간도 저장 한 다음 index URL로 리턴된다!
            return redirect('pybo:index')   # 빛의 속도로 저장한 다음 index 페이지를 띄우는 것
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)
