
from django.views.generic.base import TemplateView
from django.urls import path
from . import views
from board import views as board_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signin/', auth_views.LoginView.as_view(template_name='injo/signin.html')),   # signin은 app사용
    path('signout/', auth_views.LogoutView.as_view() ),
    path('signup/', views.signup),
    path('createUser/', views.createUser),
]