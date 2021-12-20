from django.urls import path
from . import views

app_name = 'pybo'  # 앱의 이름을 pybo로 하겠다는 뜻

urlpatterns = [  # config/urls.py에 있던 매핑 여기로 옮기고 pybo관련 매핑은 앞으로도 여기서~
    path('', views.index, name='index'),  # 질문목록매핑, name은 이 url 매핑의 별칭! 이름을 정해주는 것
    path('<int:question_id>/', views.detail, name='detail'),    # 질문상세매핑, <int:question_id> int 사용으로 숫자가 매핑됨, id에서 다 빼고 숫자만 남음
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),  # 답변 등록 매핑
    path('question/create/', views.question_create, name='question_create'),  # 질문 등록 매핑
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),  # 질문 수정 매핑
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),  # 질문 삭제 매핑
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),  # 답변 수정 매핑
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),  # 답변 삭제 매핑
    path('comment/create/question/<int:question_id>/', views.comment_create_question, name='comment_create_question'),  # 질문 댓글 작성 매핑
    path('comment/modify/question/<int:comment_id>/', views.comment_modify_question, name='comment_modify_question'),   # 질문 댓글 수정 매핑
    path('comment/delete/question/<int:comment_id>/', views.comment_delete_question, name='comment_delete_question'),   # 질문 댓글 삭제 매핑
    path('comment/create/answer/<int:answer_id>/', views.comment_create_answer, name='comment_create_answer'), # 답변 댓글 작성 매핑
    path('comment/modify/answer/<int:comment_id>/', views.comment_modify_answer, name='comment_modify_answer'), # 답변 댓글 수정 매핑
    path('comment/delete/answer/<int:comment_id>/', views.comment_delete_answer, name='comment_delete_answer'), # 답변 댓글 삭제 매핑
]
