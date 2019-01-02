# Python 03 (12/19)



- Q. 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

```python
item = int(input("번호를 입력하세요 : "))
for i in range(1,item+1):
    print(i)
```

- Q. 투자 경고 종목 리스트가 있을 때 사용자로부터 종목명을 입력 받은 후 해당 종목이 투자 경고 종목이라면

  '투자 경고 종목입니다'를 아니면 '투자 경고 종목이 아닙니다.'를 출력하는 프로그램을 작성하라.

```python
warn_imvestment_list = ["microsoft", "google", "naver", "kakao", "samsung", "lg"]
print(f"경고 종목 리스트: {warn_investment_list}")
item = input('투자종목이 무엇입니까?: ')

if item.lower() in warn_investment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")

#.lower() : 입력값에 대문자가 들어와도 소문자로 바꿔주는 것. 
# if - not in 일 때는 논리구조가 반대로 된다. 
```

-  Q. colors = ['Apple', 'Banana', 'Coconut', 'Deli', 'Ele', 'Grape']

  다음 리스트에서 0번째 4번째 5번째 요소를 지운 새로운 리스트를 생성하시오. 

> 방법1

```python
colors = ['Apple', 'Banana', 'Coconut', 'Deli', 'Ele', 'Grape']
colors2 = []
for i in range(len(colors)):
    if i in [0, 4, 5]:
        pass
    else:
        colors2.append(colors[i])
print(colors2)

```

> 방법2

```python
deletsindex = [0, 4, 5]
for i in range(0, len(colors)):
    if i not in deletsindex:
        fruit.append(colors[i])
print(fruit)
```

- Q. 1. ssafy의 semester1의 기간을 출력하세요

  2. ssafy dictionary 안에 들어 있는 '대전'을 출력하세요

  3. daejeon 의 매니저의 이름을 출력하세요

```python
ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"]
        }
    },
    "duration": {
        "semester1": "6월까지"
    },
    "classes": {
        "seoul":  {
            "lecturer": "john",
            "manager": "pro",
        },
        "daejeon":  {
            "lecturer": "tak",
            "manager": "yoon",
        }
    }
}

print(ssafy["duration"]["semester1"])

print(ssafy["location"][1])

print(ssafy["classes"]["daejeon"]["manager"])
```



## html

----

- 뼈대 - 태그이름 <h1> 은 대소문자 구별하지 않지만, 소문자 권장. 

```html
<!DOCTYPE html>   #이 문서가 html 이라는 것을 알려주는 것 
<html>
<head> #속성이 들어간다. 브라우저에 표시되지 않는다. 설정 넣는 부분. 

</head>
<body>

</body>
</html>

```

```html

<!DOCTYPE html>   
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>누구의 블로그</title>
    <link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet">

</head>
<body>
    <h1>Hello HTML</h1>
    <p>안녕하세요</p>
    <p>안녕하세요</p>
    안녕하세요<br>안녕하세요
    <hr>
    <!-- 이미지 태그 -->
    <img src="이미지 주소" alt="팬더">
    <p id="uniq" class="ssafy daejeon"></p>
</body>
</html>

```



- 
- <br> : enter
- hr : 구분선
- 



### flask

------

```python
from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route("/")
def index():
    return "안녕하세요"
    
@app.route("/hello")
def hello():
    return "오늘은 12월19일"
    

@app.route("/html_tag")
def html_tag():
    return "<h1>안녕하세요</h1>"
    
@app.route("/html_line")
def html_line():
    return """
    <h1>여러줄 보내기</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
    """
    
@app.route("/html_render")
def html_render():
    return render_template("index.html")
    
@app.route("/html_name/<string:name>")
def html_name(name):
    return render_template("hello.html", your_name = name)
    
@app.route("/math/<int:num>")
def math(num):
    result = num**3
    return render_template("math.html", your_num = num, your_result = result)
    
    
@app.route("/dinner")
def dinner():
    list = ["초밥", "탕수육", "삼겹살", "돼지국밥"]
    dict = {
        "초밥":"",
        "탕수육":"",
        "삼겹살":""
        "돼지국밥":""
    }
    pick = random.choice(list)
    url = dict[pick]
    return render_template("dinner.html", pick=pick, url=url)
    
```

