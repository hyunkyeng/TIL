## 36_homework (2019.04.23)

190501

1번. DOM에서 특정 요소를 선택할 때 document.querySelector() 뿐만 아니라 document.querySelectorAll() 역시 사용할 수 있다. 둘의 차이를 검색하여 기 술하시오.



`document.querySelector()` : 제공한 선택자 또는 선택자 뭉치와 일치하는 **문서 내 첫 번째 요소**를 반환

`document.querySelectorAll()` : 선택자를 만족하는 **모든 요소**의 목록이 필요할 때 사용



2번. JS에서 자주 사용하는 EventListener 들 중 아래와 같은 것들이 있다. 각각 간 략하게 어떤 Trigger 를 의미하는지 조사하여 간략하게 기술하시오.

```
– click : 마우스 버튼 클릭시 발생
– mouseover :마우스 커서를 올려놓았을 떄 발생
- mouseout : 마우스 커서를 올려놓았다가 밖으로 나갈 때 발생
- mousemove : 마우스 커서를 움직일 때 발생
– keypress : 키보드가 눌리는 순간 발생
- keydown : 키보드가 눌려있을 때 발생
- keyup : 키보드가 눌려있다가 떼는 순간 발생
– load : 페이지를 전부 다 읽어들인 후에 발생
– scroll : 스크롤바가 스크롤되는 경우 발생
– change : 텍스트박스의 값이 변경되는 경우 발생
```



3번. DOM 에 요소를 추가할 때, innerHTML += 의 방법과 appendChild() 함수를 통해 추가하는 방법이 있다. 둘의 차이를 간략하게 기술하시오.



`innerHTML +=` : DOM 객체의 **Property**로서 존재.   해당 DOM 객체 내부의 HTML을 주어진 인자로 교체하거나 아니면 반환. (내부 HTML을 완전히 교체)



`appendChild()` : **Method**.   인자를 DOM 객체를 받아 해당 객체의 자식리스트 맨 마지막에 더해주는 기능. (DOM 레벨에서 객체 삽입을 제어)