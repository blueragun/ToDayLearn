from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# ORM(object relation mapping)

class board( models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 반드시 인증을 해야만 글을 쓸수 있다
    createDate = models.DateField()
    # writer = models.CharField(max_length=128)
    subject = models.CharField(max_length=255)
    content = models.TextField()
    # 외래키 추가
