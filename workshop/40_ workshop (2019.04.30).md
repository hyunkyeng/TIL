# 40_ workshop (2019.04.30)

#### Vue.js





다음은 Vue 인스턴스를 사용하여 렌더링한 DOM의 결과물이다.

```
Hello, World!
```



위와 같이 렌더링 하기 위하여 필요한 (a), (b)를 작성하여 Vue 인스턴스를 완성하시오

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</head>
<body>
    <div id="app">
        {{ message }}
    </div>
    
    <script>
        var app = new Vue({
            el: '#app',
            data: {
                message: 'Hello, World!'
            },
        })
    </script>

</body>
</html>
```