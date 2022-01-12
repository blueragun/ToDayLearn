from django.shortcuts import render
from django.contrib.auth.models import User
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password



# Create your views here.
# signin 안씀 django에 기본적으로 만들어져있는 앱을 사용
#def signin( request ) :
#   return render(request, 'injo/signin.html')

def signup( request ) :
   return render(request, 'injo/signup.html')

def createUser( request ) :  # 회원가입
   id = request.POST['id']
   pw = request.POST['pw']
   user = User(username=id, password=make_password)   # 일반유저 비밀번호 hash 알고리즘 적용
   user.save()
      
   return HttpResponseRedirect(reverse('list'))

