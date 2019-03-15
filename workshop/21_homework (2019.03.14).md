# 21_homework (2019.03.14)

### Django-model



##### 1. Question 모델과 Comment 모델이 1:N관계라고 할때 하나의 Question을 보여주는 페이지에서 Comment를 모두 보여주려고 한다. 다음과 같은 detail.html이 있을때 모든 Comment의 content를 h3태그를 이용해서 출력하는 for문을 작성하세요. (related_name은 설정해주지 않았다고 가정한다.)

```html
{% extends 'base.html' %}

{% block body_block %}
<h1>{{question.title}}</h1>
<h1>{{question.author}}</h1>

{% for comment in comments %}
<h3>{{comment.content}}</h3>
{% endfor %}

{% endblock %}
```



##### 2. 다음과 같은 urls.py 파일이 있다고 가정할때 comment를 작성하는 버튼을 만들기 위해 form태그 안에 action속성값으로 넣어줘야 하는 경로를 작성하세요.

```html
<form action="{% url 'question:comments_create' question.pk %}">
    ...
</form>
```