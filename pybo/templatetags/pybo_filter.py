# 템플릿태그 디렉터리는 반드시 앱 디렉터리 하위에 생성해야함
# 장고에는 -(빼기)필터로 만들어진 함수가 따로 없기 때문에, 직접 템플릿을 만들어 함수화 시켜 사용해야한다. (직접 공식과 그 공식의 별칭을 만드는 것)
import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter    # sub 함수에 @register.filter 애너테이션을 적용하면 템플릿에서 해당 함수를 필터로 사용할 수 있음
def sub(value, arg):
    return value - arg  # sub 필터는 기존 값 value에서 입력으로 받은 값 arg를 빼서 리턴(가장 최근순으로 정렬되어있어서)


@register.filter()
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))