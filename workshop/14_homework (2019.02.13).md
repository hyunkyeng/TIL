# 14_homework (2019.02.13)



Q. 1.  Django는 요청에 대한 응답을 해줄 때 허용하는 도메인에게만 응답을 해주도록 설정한다. Settings.py 파일에서 도메인을 허용하기 위해 수정해줘야 하는 변수 이름을 찾아서 적어주세요

```
ALLOWED_HOST = ['주소']
```



Q. 2. https://<your-server-url>/ssafy 로 요청이 들어왔을때 응답을 해주기 위해 urls.py에 추가해주어야 할 코드를 작성하세요 (실행하는 함수는 views.py 안에 있는 ssafy 함수라고 가정한다.)

```
from home import views

path('ssafy/', views.ssafy, name='ssafy')
```



Q. 3. Django 서버를 실행시키는 명령어를 작성해주세요 (C9환경에서)

```
python manage.py runserver $IP:$PORT
```



Q. 4. django는 MTV로 이루어진 web framework 이다. MTV가 무엇의 약자인지 작성하 세요

```
Model Template View (MVC : Model View Controller)
```



