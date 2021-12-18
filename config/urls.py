from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),    # include : 직역하면 pybo.urls를 포함하겠다는 뜻의 함수
]
