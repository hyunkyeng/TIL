## 08_homework(2019.01.11)



1.  Web에서의 커뮤니케이션 방식은 ____(a)____과(와) ____(b)____(으)로 이루어져 있다. 브라우저의 주소창에 주
      소를 입력하는 것으로 ____(a)____을(를) 보내며, 그에 대한 ____(b)____(으)로 HTML, XML, JSON 등의 문서
      를 보내준다. 각각 (a)와 (b)에 들어갈 말을 작성하시오.

a : request, b : response



2.  Flaks Web Framework는 Python에 내장되어 있는 모듈이 아니므로 별도의 설치가 필요하다. Flask를 설치
    하기 위하여 bash에서 어떤 명령어를 입력해야 하는지 작성하시오.

```
pip install Flask
```



3.  다음은 가장 기본적인 구조의 Flask 코드이다. (a)에 들어갈 코드를 작성하고, 이 코드가 의미하는 것을 설명
    하시오.

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
```

from flask import Flask : flask 안의 내장함수를 불러오는 것을 의미한다. 



4.  3번 문제에 작성된 Flask 코드가 app.py라는 이름으로 저장되어 있으며 bash의 현재 위치는 app.py가 있는
    곳과 동일하다. 이 때, Flask 서버를 실행하기 위하여 어떤 명령어를 입력해야 하는지 작성하시오.

```python
flask run
```

