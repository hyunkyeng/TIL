# 43_workshop (2019.05.02)
※ v-bind와 v-model 디렉티브를 활용하여, 다음와 같이 'Go!' 링크를 누르면 입력 창에 작성한 URL로 가도록 하는 '주소가 변하는 링크'를 만들어 봅시다.
```markdown
`https://www.google.com`Go!
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
        <input type="text" v-model="urls"><a v-bind:href="urls">Go!</a>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        const app = new Vue({
            el:'#app',
            data: {
                urls: '',
            },  
        })
    </script>
</body>
</html>
```