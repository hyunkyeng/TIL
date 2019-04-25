## 30_homework (2019.04.09)



![1556154381456](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1556154381456.png)



```python
class Post(models.Model):
    content = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.[빨간박스](settings.AUTH_USER_MODEL, [초록박스]='like_post_set', blank=True)
```


1.  Post 모델과 User모델을 M:N 관계로 설정 하여 좋아요 기능을 구현하려고 한다. 이때 빨간색 박스에 들어갈 클래스의 이름은 무엇인가?

   `ManyToMany`

   

2.  좋아요 기능을 구현하기 위하여 User모델과 M:N관계설정을 하려고 한다. 그런데 user 칼럼에서 이미 User모델과 관계설정이 되어있기 때문에 이를 구분하기 위해 초록색 박스에 들어갈 옵션은 무엇인가?

   `related_name`