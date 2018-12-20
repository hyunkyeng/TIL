# pyrhon_04 (12/20)



### #파이썬 dictionary 활용 기초

```python
dict = {
    "대전": 23,
    "서울": 30,
    "구미": 20
}

print(dict.values())
print(type(dict.values()))
```

- 답 : dict_values([23, 30, 20])

- 답 : <class 'dict_values'>



- Q. 평균을 구하세요

> 1.

```python
scores = {
    "국어": 87,
    "영어": 92,
    "수학": 40
}

# value = score.values()
# print(value)

total_score = 0
for score in scores.values():
    # total_score = total_score + score 와 밑에 문장은 같은 문장이다. 
    total_score += score
```

> 2.

```python
scores = {
    "국어": 87,
    "영어": 92,
    "수학": 40
}

average_score = total_score / len(scores)   
print(total_score)
print(average_score)
```



- Q. 반평균을 구하세요.

```python
scores = {
    "철수": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    },
    "영희": {
        "수학": 70,
        "국어": 60,
        "음악": 50
    }
}

# total_score = 0
# print(scores.values())
all_total = 0
count = 0
for score in scores.values():
    totals = score.values()
    # print(totals)
    for total in totals:
        all_total += total
        count += 1


average_score = all_total / count       
print(all_total)
print(average_score)

```

> 답.   450 
>
> ​	75.0

> 선생님 풀이

```python
total_score = 0
count = 0
for person_score in scores.values():
    for indivisual_score in person_score.values():
        total_score += indivisual_score
        count += 1

print(total_score)
average_score = total_score / count
print(average_score)
```



### #주요개념

```python
scores = {
     "국어": 87,
     "영어": 92,
     "수학": 40
}

for key, value in scores.items():
    print(key)
    print(value)
```

> 실행 : 
>
> 국어
> 87
> 영어
> 92
> 수학
> 40



-  Q.3 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

> 내 풀이

```python
cities = {
    "서울": [-6, -10, 5],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9]
}

max_city = 0
min_city = 0
max_name = ""
min_name = ""
for name, temp in cities.items():
    tempmax = max(temp)
    if max_city < tempmax:
        max_city = tempmax
        max_name = name
    tempmin = min(temp)
    if min_city > min(temp):
        min_city = min(temp)
        min_name = name
print(max_city)
print(max_name)
print(min_city)
print(min_name)

print(f"가장 더웠던 곳은 {max_name}, 가장 추웠던 곳은 {min_name}")

```



> 선생님 풀이

```python
cities = {
    "서울": [-6, -10, 5],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9]
}

hot = 0
cold = 0
hot_city = ""
cold_city = ""
count = 0

for name, temp in cities.items():
    # name = "서울"
    # temp = [-6, -10, 5]
    if count == 0:
        hot = max(temp)
        cold = min(temp)
        hot_city = name
        cold_city = name
    else:
        # 최저 온도가  cold 보다 더 추우면, cold  에 넣고
        if min(temp) < cold:
            cold = min(temp)
            cold_city = name
        # 최고 온도가 hot 보다 더 더우면, hot  에 넣고
        if max(temp) > hot:
            hot = max(temp)
            hot_city = name
    count += 1

print(f"{hot_city}, {cold_city}")
```





### #Flask

- lotto

> hello.py

```python
@app.route("/lotto")
def lotto():
    num_list = list(range(1,46))
    lucky = random.sample(num_list, 6)
    return render_template("lotto.html", lucky=lucky)
```

> lotto.html

```python
<h2>{{ lucky }}</h2>
{% for num in lucky %}
{{ num }}
{% endfor %}
```

> 결과 (http://flask-basic-hyunkyeng.c9users.io:8080/lotto)

## [39, 40, 44, 42, 6, 10]

39 40 44 42 6 10



- 검색창 ( 네이버 )

> hello.py

```python
@app.route("/naver")
def naver():
    return render_template("naver.html")
```

> naver.html  
>
> > 네이버 검색창에서 검색한 후에 어디까지는 있어야 검색이 가는한지 확인한다. 네이버는 https://search.naver.com/search.naver?&query=   여기까지! query 뒤에 검색어를 넣으면 검색이 되므로 query 는 name 에 넣는다.
> >
> > form 을 작성하고 엔터를 치면 저 형태가 나온다. 

```python
<h1>네이버 검색</h1>
<form action="https://search.naver.com/search.naver">
    <input type="text" name="query"/>
    <input type="submit" value="Submit"/>
</form>

```

> 결과 (http://flask-basic-hyunkyeng.c9users.io:8080/naver)



- 검색창 ( 구글 )

> hello.py

```python
@app.route("/google")
def google():
    return render_template("google.html")
```

> google.html
>
> > 구글 검색창에서 검색한 후에 어디까지는 있어야 검색이 가는한지 확인한다. 구글은 https://www.google.com/search?q=   여기까지! q 뒤에 검색어를 넣으면 검색이 되므로 q 는 name 에 넣는다.

```python
<h2>구우우우우글</h2>
<form action="https://www.google.com/search">
    <input type="text" name="q"/>
    <input type="submit" value="Submit"/>
</form>
```

> 결과 (http://flask-basic-hyunkyeng.c9users.io:8080/google)