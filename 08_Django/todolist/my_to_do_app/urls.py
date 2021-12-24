from django.urls import path
from . import views  # view와 연결

urlpatterns = [
    path('', views.index, name='index'),
    path('createTodo/', views.createTodo),   #createTodo에 대한 url요청과 view와 연결
]
