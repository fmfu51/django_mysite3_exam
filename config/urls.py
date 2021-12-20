from django.contrib import admin
from django.urls import path, include

from pybo.views import base_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),    # include : 직역하면 pybo.urls를 포함하겠다는 뜻의 함수
    path('common/', include('common.urls')),    # config의 url에 인클루드로 연결
    path('', base_views.index, name='index'),  # '/' 에 해당되는 path
]
