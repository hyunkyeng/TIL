## 31_workshop (2019.04.10)



- 데이터베이스에 값을 추가할 때, 아래와 같이 검증하려고 한다. 적절한 코드를 작성하
  시오.

![1556160399479](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1556160399479.png)

![1556160404756](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1556160404756.png)



```
from django.db import models
from django.core.validators import EmailValidator, MinValueValidator

# Create your models here.
class Person(models.Model):
    last_name = models.CharField(max_length=40)
    email = models.CharField(max_length=100,
                                validators = [EmailValidator(message='이메일 형식에 맞지 않습니다.')])
                                
    age = models.IntegerField(validators =[MinValueValidator(limit_value=20, message='미성년자 ㄴㄴ')] )
```

