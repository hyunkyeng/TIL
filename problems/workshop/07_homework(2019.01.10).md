

1. 파이썬에서은 객체지향프로그래밍 언어입니다.
  파이썬에서 기본적으로 정의된 클래스 5개만 작성해보세요.

str, int, list, complex, dict



2. 다음 중 틀린 것은? (3)

   (1) 클래스 내에 정의된 멤버 함수는 ‘메서드(method)’라고 부른다.
   (2) 클래스는 선언과 동시에 클래스 객체가 생성되며, 인스턴스 객체를 만들면 클래스에서 선언된 메서드를
   활용할 수 있다.
   (3) isinstance(인스턴스 객체, 클래스 객체)를 활용하면 상속 관계까지 확인 가능하다.
   (4) 생성자는 인스턴트 객체가 생성될 때 자동으로 호출된다.
   (5) 숫자 5는 그냥 숫자일 뿐 클래스가 없다. (o- 숫자 5는 독립된 객체)



3. Person 클래스를 정의하고,
  이름이 ‘홍길동’, 나이가 20인 p1 인스턴스 객체를 만들어보세요.
  이름이 ‘둘리’, 나이가 0인 p2 인스턴스 객체를 만들어보세요.
  ​		인스턴스 속성 : name, age
  ​		메서드 : greeting()
  인스턴스 생성시 이름과 나이를 받으며, 나이가 없는 경우 0으로 설정한다.
  greeting이 호출되면, 아래와 같이 문자열을 반환한다.

```python
class Person:
    def __init__(self, name, age=0):   #__init__ : 생성자  #self 는 클래스 Person
        self.name = name
        self.age = age
    def greeting(self):   #위의 self와 아래의 self는 다르다. 
        print(f'안녕하세요. {self.name}. {self.age}살 입니다.')
```

```python
p1 = Person('홍길동', 20)   #기본값을 설정할 수 있다.
p1.greeting()
```

out: 안녕하세요. 홍길동. 20살입니다.

```python
p2 = Person('둘리')
p2.greeting()
```

out: 안녕하세요. 둘리. 0살입니다.