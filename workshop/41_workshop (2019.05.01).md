# 41_workshop (2019.05.01)

※  다음과 같은 Vue 인스턴스가 있을 때, v-for와 v-if 디렉티브를 활용하여 짝수만 나타나 도록 하는 리스트를 만들어 봅시다.

```html
var app = new Vue({
	el:'#app',
	data: {
		numbers: [0,1,2,3,4,5,6,7,8,9,],
	},	
})
```

```markdown
- 0
- 2
- 4
- 6
- 8
```



```html
<div id="app">
    <li v-for="number in numbers" v-if="number % 2 === 0">
        {{ number }}
    </li>
</div>
```