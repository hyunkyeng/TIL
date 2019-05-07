# 36_workshop (2019.04.23)
190501
- 아래 Instruction 에 따라 JS 코드를 작성해 보자.
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Clicked</title>
</head>
<body>
    <h1>0</h1>
    <button id="change-btn">
        Click it
    </button>
    <script>
    // #change-btn 을 button 상수에 할당한다.
        const button = document.querySelector('#change-btn')
    // h1 태그를 header 상수에 할당한다.
        const header = document.querySelector('h1')
    // clickCount 변수를 0으로 초기화 한다.
        let clickCount = 0
    // button 에 'click' eventListner를 추가한다.
        // clickCount 가 1씩 올라간다.
        button.addEventListener('click', event => {
            clickCount += 1
        // header 안의 내용을 clickCount 로 바꾼다.
            header.innerText = clickCount
        })
    </script>
</body>
</html>
```