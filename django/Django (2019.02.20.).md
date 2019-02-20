# Django (2019.02.20.)







똑같이 설정 후



app폴더(Boards)의 model.py

```
from django.db import models

# Create your models here.
class Board(models.Model):    # 각 모델은 django.db.models.Model 클래스의 서브 클래스로 표현 
    title = models.CharField(max_length=10)     # max_length 는 charfield의 필수인자.
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  #UTC
    updated_at = models.DateTimeField(auto_now=True)
    #auto_now_add=True : 장고 모델이 최초저장시에만 현재 날짜를 적용
    #auto_now=True : 장고모델이 save 될때마다 현재 날짜로 갱신
```



settings.py

```
USE_TZ = False         #이렇게 해야 기본적으로 LANGUAGE_CODE = 'ko-kr', TIME_ZONE = 													'Asia/Seoul' 이 전체다 설정된다.
```



bash - 확인하는 것

```
python manage.py makemigrations boards
```

--> Migrations for 'boards':
  boards/migrations/0001_initial.py

   Create model Board  이라고 뜬다



- (0001_initial.py : db 에 아직 들어가지 않은 설계도)



bash - 확인하는 것

```
python manage.py makemigrations boards
```

--> Migrations for 'boards':
  boards/migrations/0002_board_updated_at.py
   Add field updated_at to board   이라고 뜬다.



----

아직 db에 반영되지 않은것. 

db에 반영하려면 bash  -> table이 만들어진다. 

```
python manage.py migrate
```



----

db 에 잘만들어졌는지 확인하려면

bash

```
sqlite3 db.sqlite3
```

```
sqlite> .table    # table확인
```

```
sqlite> .schema boards_board   #schema확인
```

```
sqlite> .exit
```



----

bash창에서 직접 조작 ( 테이블 조작 ) - 장고orm(장고문법)

bash

```
python manage.py shell
>>> from boards.models import Board
>>> Board.objects.all()

>>> board = Board()		#인스턴스생성
>>> board = Board()
>>> board.title = 'first'
>>> board.content = 'django!'
>>> board.save()
>>> Board.objects.all() 	#확인하는것
>>> exit()
```



models.py 에 추가

```
    def __str__(self):
        return f'{self.id}: {self.title}'
```



bash

```
python manage.py shell
>>> from boards.models import Board
>>> Board.objects.all()  #확인하는 것 : <QuerySet [<Board: 1: first>]>
>>> exit()
```



bash

```
pip install django-extensions
```

- 확장프로그램을 깔면 settings를 조작해야한다. 

settings.py에 들어가서  INSTALLED_APPS = [
​    'boards.apps.BoardsConfig', 밑에 추가

```
    'django_extensions',
```



bash - 2번째 방법

```
$ python manage.py shell_plus

>>> board = Board(title='second', content='django!!')	#아직 저장 안된것.
>>> board.save() 	#db에 저장됨
>>> board.objects.all()  	#확인 : <QuerySet [<Board: 1: first>, <Board: 2: second>]>
```



bash - 3번째방법

```
>>> Board.objects.create(title='third', content='django!!!')  #create에 save기능이 있기 때문에 save안해줘도 된다. -> <Board: 3: third>
```



진짜 save를 안하면 저장이 안되는지 확인

```
>>> board = Board()
>>> board.title = 'fourth'
>>> board.content = 'django!!!!'

>>> board.id     			#아무것도 안뜬다
>>> board.created_at		#아무것도 안뜬다

>>> board.save()
>>> board.id
4						# 이제 뜬다
>>> board.created_at
datetime.datetime(2019, 2, 20, 10, 35, 24, 858073)			# 이제 뜬다
```



title을 10자로 정했는데 더 긴 글자가 들어가면

```
>>> board = Board()
>>> board.title = 'asdlfkjsldkjfl'
>>> board.full_clean()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/ubuntu/.pyenv/versions/django-venv/lib/python3.6/site-packages/django/db/models/base.py", line 1152, in full_clean
    raise ValidationError(errors)
django.core.exceptions.ValidationError: {'title': ['이 값이 최대 10 개의 글자인지 확인하세요(입력값 14 자).'], 'content': ['이 필드는 빈 칸으로 둘 수 없습니다.
```



## READ



전체조회

```
>>> Board.objects.all()
<QuerySet [<Board: 1: first>, <Board: 2: second>, <Board: 3: third>, <Board: 4: fourth>]>
```

특정 제목만 조회

```
>>> Board.objects.filter(title='first').all()
<QuerySet [<Board: 1: first>]>

>>> Board.objects.filter(title='first').first()  # 이렇게 하는게 더 정확하다.
<Board: 1: first>
```



1번 글 조회

```
>>> Board.objects.filter(title='missing').first()
>>> board = Board.objects.get(pk=1)    # .get으로 가져와야된다. 
>>> board
<Board: 1: first>
```



fi 가 들어간 제목 조회

```
<QuerySet [<Board: 1: first>]>
>>> boards = Board.objects.filter(title__contains='fi').all()
>>> boards
<QuerySet [<Board: 1: first>]>
```



fi 로 시작하는 제목 조회

```
>>> boards = Board.objects.filter(title__startswith='fi')
>>> boards
<QuerySet [<Board: 1: first>]>
```



!로 끝나는 content 조회

```
>>> boards = Board.objects.filter(content__endswith='!')
>>> boards
<QuerySet [<Board: 1: first>, <Board: 2: second>, <Board: 3: third>, <Board: 4: fourth>]>
```



정렬

오름차순

```
boards = Board.objects.order_by('title').all()

>>> boards
<QuerySet [<Board: 1: first>, <Board: 2: second>, <Board: 3: third>, <Board: 4: fourth>]>
```

내림차순

```
>>> boards = Board.objects.order_by('-title').all()

>>> boards
<QuerySet [<Board: 3: third>, <Board: 2: second>, <Board: 4: fourth>, <Board: 1: first>]>
```



업데이트

```
>>> board = Board.objects.get(pk=1)
>>> board.title = 'hello'
>>> board.save()
>>> board.title
'hello'
```



지우기 - 위에서 save된게 사라진다.

```
>>> board.delete()
(1, {'boards.Board': 1})
```



--------------

view.py

```
# Create your views here.
def index(request):
    return render(request, 'boards/index.html')

```

crud폴더에 있는 urls.py

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('boards/', include('boards.urls')),
    path('admin/', admin.site.urls),
]

```

boards폴더에 urls.py 새로만들기

```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

boards폴더에 templates폴더 만들고 그 안에 boards 폴더 만들기

그 폴더에 base.html 만들기

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
    <title>게시판</title>
</head>
<body>
    <div class="container">
        {% block body %}
        {% endblock %}
    </div>
   
    
    
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
</body>
</html>
```

index.html 만들기

```
{% extends 'boards/base.html' %}
{% block body %}
    <h1>Board</h1>
    <a href="#">글 작성하기</a>
    <hr>
{% endblock %}
```











--------

관리자 모드

bash

```
$ python manage.py createsuperuser
사용자 이름 (leave blank to use 'ubuntu'): admin
이메일 주소: hyunk4593@gmail.com
Password: 
Password (again): 
Superuser created successfully.
```

boards에 admin.py

```
from django.contrib import admin
from .models import Board

# Register your models here.
admin.site.register(Board)
```

http://django-intro-hyunkyeng.c9users.io:8080/admin

으로 들어가서 쉽게 추가, 변경, 삭제 가능 

이렇게 하면 id값, 제목만보인다



내용이 보이려면

admin.py 에 클래스를 만들어줘야 한다. 

```
from django.contrib import admin
from .models import Board

# Register your models here.
class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at', 'updated_at',)
    
    
admin.site.register(Board, BoardAdmin)
```























