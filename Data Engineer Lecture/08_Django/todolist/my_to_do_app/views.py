from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

# 미리 만들어진 model을 가져오기
from .models import *


# Create your views here.
def index( request ) :
    #DB의 내용을 브라우저에 전달하기 위한 코드를 추가
    todos = Todo.objects.all()   # 테이블 내의 모든 내용을 조회 투두스를 커리셋형태로 함
    content = {'todos':todos}    # 딕셔너리 형태로 한 후 아래 리턴문의 content로 보내준다
    return render(request, "my_to_do_app/index.html", content)


def createTodo( request ) :
# url과 view가 잘 연결되었는지를 확인하기 위해서 아래와 같은 코드 사용
#def createTodo( request ) :
#    return HttpResponse('create Todo를 할래')

# 사용자가 입력한 할 일을 잘 받아오는지 확인
# 입력값 전달은 post 방식으로, 'todoContent'변수를 통해서 전달될 것임
#    user_input_str = request.POST['todoContent']
#    return HttpResponse(f'사용자가 입력한 값 : {user_input_str}')

    user_input_str = request.POST['todoContent']
    # models.py에서 정의된 클래스를 이용해서 전달받은 겂을 DB에 저장
    new_todo = Todo( content = user_input_str )
    new_todo.save()
    
    return HttpResponseRedirect(reverse('index'))

def deleteTodo( request ) :
    # print( '요청변수:', request.GET['todoNum'] )
    todo = Todo.objects.get(id=request.GET['todoNum'])
    todo.delete()
    return HttpResponseRedirect(reverse('index'))
    