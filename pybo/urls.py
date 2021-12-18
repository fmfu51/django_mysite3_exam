from django.urls import path
from . import views

urlpatterns = [     # config/urls.py에 있던 매핑 여기로 옮기고 pybo관련 매핑은 앞으로도 여기서~
    path('', views.index),
    path('<int:question_id>/', views.detail),   # <int:question_id> int 사용으로 숫자가 매핑됨, id에서 다 빼고 숫자만 남음
]