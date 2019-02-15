# Django (2019.02.14)



### 기존에 utilities 앱을 새로 만든다

앱만들면 그 앱안에 urls.py를 만들고 

settings.py INSTALLED_APPS 맨 밑에 추가

```
'utilities.apps.UtilitiesConfig',
```





기존의 urls.py

```
from django.contrib import admin
from django.urls import path, include
# from home import views


urlpatterns = [
    path('home/', include('home.urls')),   #home으로 들어오면 home.urls를 호출한다. 
    path('admin/', admin.site.urls),
]
```



앱안의 urls.py

```
from django.urls import path
from . import views  # 자기의 view를 불러오는 것\


urlpatterns = [
    path('static_example/', views.static_example, name='static_example'),
    path('template_example', views.template_example, name='template_example'),
    path('user_create/', views.user_create, name='user_create'),
    path('user_new/', views.user_new, name='user_new'),
    path('pong/', views.pong, name='pong'),
    path('ping/', views.ping, name='ping'),
    path('cube/<int:number>/', views.cube, name='cube'),
    path('hello/<name>/', views.hello, name='hello'),
    path('dinner/', views.dinner, name='dinner'),
    path('index/', views.index, name='index'),
    
]
```



- utilities 앱 시작 

views.py  추가

```
def index(request):
    return render(request, 'index.html')
```

기존 urls.py   추가

```
urlpatterns = [
    path('utilities/', include('utilities.urls')),
```

utilities urls.py

```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),    
]
```

templates 폴더 만들고, index.html 파일 만들기

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Utilites</title>
</head>
<body>
    <h1>실습실습</h1>
</body>
</html>
```



기존 templates 폴더 안에 기존앱인 home 폴더를 만들어서 templates에 있는 html을 home폴더로 옮긴다. 



기존 static 에도 안에 home만들어서 다 옮긴다. 



home의 views에 들어가서 모든 함수의  'index.html' 에 home/ 추가 ->

```
'home/index.html'
```





django_intro 폴더안에 templates폴더를 생성후 기존의 base.html을 templates폴더로 옮긴다.



settings에 TEMPLATES = [
​    {
​        'DIRS': [os.path.join(BASE_DIR, 'django_intro', 'templates')],

추가하면 base.html이 가장먼저 인식된다. 



project에 있는 static폴더를 사용할때 

STATICFILES_DIRS = [

​	os.path.join(BASE_DIR, "프로젝트이름쓰기", "static")

]























