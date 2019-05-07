# 42_workshop (2019.05.02)

※ v-on 디렉티브를 활용하여, 다음과 같이 ‘+1’ 버튼을 누르면 숫자가 하나씩 증가하는 Counter 앱을 만들어 봅시다.

```markdown
`+1`
Counter: 4
```



```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <div id="app">
        <h1>Counter: {{ count }}</h1>
        <button v-on:click="plus">+1</button>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        const app = new Vue({
            el:'#app',
            data: {
                count: 0,
            },
            methods: {
                plus: function () {
                    this.count++
                }
            }	
        })
    </script>
</body>
</html>
```