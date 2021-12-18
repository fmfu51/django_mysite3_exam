from django.http import HttpResponse

def index(request): # request : index함수의 매개변수
    return HttpResponse("안녕하세요. pybo에 오신 것을 환영합니다.") # HttpResponse는 요청한 페이지에 응답을 할 때 사용하는 장고 클래스
