# 17_workshop (2019.02.20)



Q. 자신의 반에 있는 사람들의 데이터를 저장하는 Student 모델을 생성합니다. 

Student모델이 가져야 할 필드는 아래와 같습니다. 

name(이름) : CharField

email(이메일) : CharField

birthday(생년월일) : DateField

age(나이) : IntegerField

- 모델 마이그레이션 작업을 거친 후 Admin페이지에서 주변학생들의 이름을 세명 저장합니다. 
- 저장 후 Admin페이지에서 





app폴더의 model.py

```:
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    birthdat = models.DateField()
    age = models.IntegerField()
    
    def __str__(self):
    	return f'{self.name}'
```



```
>python manage.py makemigrations boards
```

```
>python manage.py migrate
```





admin.py

```
from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'birthday', 'age',)
	
admin.site.register(Board, BoardAdmin)
```

```
>python manage.py createsuperuser
```



admin 페이지로 들어가기 -> 추가하기







