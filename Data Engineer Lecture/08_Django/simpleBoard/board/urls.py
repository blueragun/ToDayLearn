from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='list' ),
    path('write/', views.write, name='write' ),
    path('create/', views.create , name='create'),
    path('deleteBoard/', views.deleteBoard, name='deleteBoard'),
    path('update/', views.update, name='update'),
    path('modify/', views.modify, name='modify'),
    path('view/', views.view, name='view'),
    path('comment/', views.comment),
]
