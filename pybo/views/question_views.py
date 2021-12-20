from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import QuestionForm
from ..models import Question


@login_required(login_url='common:login')
def question_create(request):  # pybo 질문 등록
    if request.method == 'POST':
        form = QuestionForm(request.POST)  # request.POST에는 화면에서 사용자가 입력한 내용들이 담겨있음
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user  # 현재 로그인한 계정이 글쓴이가 되므로 requset.user로 작성
            question.create_date = timezone.now()
            question.save()  # 입력한 질문데이터를 저장, 시간도 저장 한 다음 index URL로 리턴된다!
            return redirect('pybo:index')  # 빛의 속도로 저장한 다음 index 페이지를 띄우는 것
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


@login_required(login_url='common:login')
def question_modify(request, question_id):  # 질문 수정
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


@login_required(login_url='common:login')
def question_delete(request, question_id):  # 질문 삭제
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)
    question.delete()
    return redirect('pybo:index')