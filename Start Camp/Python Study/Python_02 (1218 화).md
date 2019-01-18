# Python_02 (12/18 화)

#### <파일 읽고 쓰기>

### string_test_01.py

----



- python 과거 쓰던 방식 (가로 안에 one two 만 쉽게 변경 가능)
  - '일은 영어로 %s, 이는 영어로 %s' % ('one', 'two')

-  pyformat
  - '{} {}'.format('one','two')

```python
name = '이현경'
e_name = 'hyunkyeng'

print('안녕하세요. {}입니다. My name is {}'.format(name, e_name))
print('안녕하세요. {1}입니다. My name is {0}'.format(e_name, name))
print('안녕하세요. {1}입니다. My name is {1}'.format(e_name, name))
```

- f-string python 3.6

```python
name = '이현경'
e_name = 'hyunkyeng'

print(f'안녕하세요. {name}입니다. My name is {e_name}.')
```

- Q. 로또

```python
import random
num = list(range(1,46))
box = random.sample(num,6)
lotto = sorted(random.sample(num,6))
print(box)
print(lotto)
```

- Q. 로또 - pyformat 을 사용

```python
import random
num = range(1,46)
box = sorted(random.sample(num,6))
print("로또번호는 {}입니다".format(box))
```



### ch_name.py

-----



- 파일 이름 변경하기

```python
import os
#바꾸고 싶은 파일 위치를 복붙해오기
os.chdir(r"C:\Users\student\Desktop\TIL\dummy")
#위랑 같은 위치에 있으므로 "." 으로 표기
for filename in os.listdir("."):
    os.rename(filename, "SAMSUNG " + filename)
```

- SAMSUNG -> SSAFY 로 변경하기

```python
import os 
os.chdir(r"C:\Users\student\Desktop\TIL\dummy")
for filename in os.listdir("."):
    os.rename(filename,filename.replace("SAMSUNG","SSAFY"))
```



### make_txt.py

-----



- 파일을 새로 만들면서 열고 쓰고 닫기

  > 쓸때는 'w' , 읽을 때는  'r'

  ```python
  f = open("new.txt", "w")
  f.write("Hello !!!")
  f.close()
  ```



  > with문 이용 - 한번에 처리하기(자동으로 파일 닫아진다.)

  ```python
  with open("new.txt", "w") as f:
  	f.write("HI !!!")
  ```



-  파일을 읽은 후 프린트하기

    f = open("new.txt", "r")
    data = f.read()
    print(data)
    f.close()	



> for문으로 여러문장 쓰기 

```python
f = open("new.txt", "w", encoding = 'utf-8')
numbers = range(1,11)
for number in numbers:
    data = f'{number}번째 줄입니다.\n'
	f.write(data)
f.close()
```



> for i in range(5)  로 간단하게 사용가능

```python
f = open("new.txt", "w", encoding = 'utf-8')
for i in range(5):
    data = f'{i}번째 줄입니다.\n'
    f.write(data)
f.close()
```



> with으로 작성

```python
with open("new.txt", "w", encoding = 'utf-8') as f:
    for i in range(5):
	data = f'{i}번째 줄입니다.\n'
	f.write(data)
```



- writelines 사용

```python
menu = ["카레\n", "짜장\n", "탕수육\n"]
f = open("menu.txt", "w", encoding = 'utf-8')
f.writelines(menu)
f.close
```

> with으로 작성

```python
menu = ["햄버거\n", "짜장\n", "탕수육\n"]
with open("menu.txt", "w", encoding = 'utf-8') as f:
    f.writelines(menu)
```



- f 이용 

Q. txt파일 만들어서 "*번째 줄입니다." 프린트 - for문 사용

```python
f = open("number.txt", "w", encoding = 'utf-8')
for i in range(1,6):
	data = f'{i}번째 줄입니다.\t'
    f.write(data)
f.close()
```

Q. txt파일 만들어서 "*번째 줄입니다." 프린트 - with문 사용

```python
with open("number.txt", "w", encoding = 'utf-8') as f:
    for i in range(1,6):
        data = f'{i}번째 줄입니다.\t'
        f.write(data)
```



- readline() : 한 줄로 읽어서 리턴
- readlines() : 파일 전체를 읽어 list 형태로 리턴



- 공백지우는 방법

  - ssafy = "              sdweqq       "

  - ssafy.lstrip()
    -> 'sdweqq       '
  - ssafy.rstrip()
    -> '              sdweqq'
  - ssafy.strip()
    -> 'sdweqq'



- readlines() 사용해서 txt 읽기

```python
with open("number.txt", "r", encoding = 'utf-8') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())
```







### git 사용

----



- cd Desktop/TIL   (master 라고 뜨면 git이 그 파일을 관리한다는 것)
- git add . 
- git status   (git 의 상태 확인)
- git commit -m "second commit"
- git log  (commit 상태 확인)





### 정보 스크랩핑

------

- requests.get("https://www.naver.com") : 주소에 요청을 보내 가져오는



- 네이버 금융에서 kospi 찾기

```python
import requests
from bs4 import BeautifulSoup

req = requests.get("https://finance.naver.com/sise/").text
soup = BeautifulSoup(req, 'html.parser')
kospi = soup.select_one("#KOSPI_now")
print(kospi.text) 

```

- 네이버 부동산에서 지역별 부동산정보 찾기

```python
import requests
from bs4 import BeautifulSoup

req = requests.get("https://land.naver.com/isale/").text
soup = BeautifulSoup(req, 'html.parser')
bu = soup.select_one("#selectedDvsn")
print(bu.text)
```

- 실시간 검색어
  - #은 ID

```python
import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.naver.com/").text
soup = BeautifulSoup(req, 'html.parser')
search = soup.select_one("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul")
print(search.text)
```

- for 문 사용
  - . 은 class

```python
import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com/"
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')

for tag in soup.select('.PM_CL_realtimeKeyword_rolling .ah_item'):
    rank = tag.select_one('.ah_r').text
    name = tag.select_one('.ah_k').text
    print(f'{rank}는 {name}입니다.')
```

