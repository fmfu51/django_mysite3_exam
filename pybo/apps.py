from django.apps import AppConfig


class PyboConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pybo'   # pybo 앱을 settings.py 에 추가하면 자동으로 생기는 코드들