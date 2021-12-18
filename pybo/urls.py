from django.urls import path
from . import views

urlpatterns = [     # config/urls.py에 있던 매핑 여기로 옮기고 pybo관련 매핑은 앞으로도 여기서~
    path('', views.index),
]