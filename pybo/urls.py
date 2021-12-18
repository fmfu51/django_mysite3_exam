from django.urls import path
from . import views
app_name = 'pybo'   # 앱의 이름을 pybo로 하겠다는 뜻

urlpatterns = [     # config/urls.py에 있던 매핑 여기로 옮기고 pybo관련 매핑은 앞으로도 여기서~
    path('', views.index, name='index'),    # 질문목록매핑, name은 이 url 매핑의 별칭! 이름을 정해주는 것
    path('<int:question_id>/', views.detail, name='detail'),   # 질문상세매핑, <int:question_id> int 사용으로 숫자가 매핑됨, id에서 다 빼고 숫자만 남음
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),    # 답변 등록 매핑
    path('question/create/', views.question_create, name='question_create'),    # 질문 등록 매핑
]