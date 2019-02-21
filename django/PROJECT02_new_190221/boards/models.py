from django.db import models

# Create your models here.
class Board(models.Model):    # 각 모델은 django.db.models.Model 클래스의 서브 클래스로 표현 
    title = models.CharField(max_length=10)     # max_length 는 charfield의 필수인자.
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  #UTC
    updated_at = models.DateTimeField(auto_now=True)
    #auto_now_add=True : 장고 모델이 최초저장시에만 현재 날짜를 적용
    #auto_now=True : 장고모델이 save 될때마다 현재 날짜로 갱신
    
    
    def __str__(self):
        return f'{self.id}: {self.title}'