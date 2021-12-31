from django.contrib.auth import authenticate
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import board

# Create your views here.

def index( request ) :
   # db의 board 테이블의 모둔 내용을 가져옴
   rows = board.objects.all()
   cont = {'rows':rows}
   return render( request, 'board/list.html', cont)
   # return render(request, 'board/list.html')


def write( request ) :
   return render( request, 'board/write.html')
   # return render(request, 'board/write.html')
   
from django.contrib.auth.decorators import login_required

# 데코레이터를 이용해서 로그인이 필요한 함수
# 아래 크리에이터는 로그인이 필요함

@login_required(login_url='/injo/signin/')
def create( request ) :
 if request.method == 'POST' :
   new = board(  # DB상에 데이터를 저장하는 것
       user       = request.user,
       createDate = request.POST["createDate"],
       subject    = request.POST["subject"],
       content    = request.POST["content"],
   )
   new.save()
   return HttpResponseRedirect(reverse('list'))

 else :  # 로그인이 되어 있지 않은 경우 로그인 이후에 새로 글을 작성해줍시다.
   return render(request, 'board/write.html')
       
# 실습예제
@login_required(login_url='/injo/signin/')
def update( request ) :  # 수정
   post = board.objects.get(id=request.GET['id'])
   content = {'post' : post}
   return render( request, 'board/update.html', content)


from django.contrib import messages

@login_required(login_url='/injo/signin/')
def modify( request ) :  # 수정 후 등록
   post = board.objects.get(id=request.POST['id'])
   if request.user != post.user:
     return render(request, 'board/alert.html')
   else :
      post.createDate = request.POST['createDate']
      post.writer     = request.POST['user']
      post.subject    = request.POST['subject']
      post.content    = request.POST['content']   
      post.save()
   return HttpResponseRedirect(reverse('list'))


@login_required(login_url='/injo/signin/')
def deleteBoard( request ) :  # 삭제
   board_id = board.objects.get(id=request.GET['BNum'])
   if request.user != board_id.user:
      return render(request, 'board/alert.html')
   else :
      board_id.delete()
   return HttpResponseRedirect(reverse('list'))


def view( request ) : # 게시글보기
   post = board.objects.get(id=request.GET['id'])
   content = {'post' : post}
   return render( request, 'board/view.html', content)

def comment( request ) :   # 댓글
    return render( request, 'board/comment.html')
 
def comview( request ) :    # 댓글 작성 후 db 저장
       # db의 board 테이블의 모둔 내용을 가져옴
   if request.method == 'POST' :
       new = board(  # DB상에 데이터를 저장하는 것
       user       = request.user,
       createDate = request.POST["createDate"],
       subject    = request.POST["subject"],
       content    = request.POST["content"],
   )
   new.save()
   return HttpResponseRedirect(reverse('view'))