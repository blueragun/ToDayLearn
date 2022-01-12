from django.db import models

# Create your models here.
# 클래스의 이름이 모델(테이블)의 이름이 됨
class Todo( models.Model ) :
    # Todo 테이블에 content 컬럼을 정의
    # 컬럼타입은 '문자'이고 최대 길이는 255다
    content = models.CharField(max_length=255)
    