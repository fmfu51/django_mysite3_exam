# 템플릿태그 디렉터리는 반드시 앱 디렉터리 하위에 생성해야함
from django import template

register = template.Library()

@register.filter    # sub 함수에 @register.filter 애너테이션을 적용하면 템플릿에서 해당 함수를 필터로 사용할 수 있음
def sub(value, arg):
    return value - arg  # sub 필터는 기존 값 value에서 입력으로 받은 값 arg를 빼서 리턴(가장 최근순으로 정렬되어있어서)