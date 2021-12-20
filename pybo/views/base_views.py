from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from ..models import Question   # 하위 디렉토리로 옮겨서 경로가 한번 더 늘어났으니 .이 하나 더!


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