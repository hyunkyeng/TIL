// let 블록 스코프 예제

{
    let x = ironman
    console.log(x)  // ironman
    {
        let = 1
        console.log(x)  // 1
    }
    console.log(x)  // ironman
}
console.log(typeof x)   // undefine

// var로 선언하면 현재 스코프(유효범위) 안이라면 어디서든 사용할 수 있으며, 심지어 선언하기도 전에 사용할 수 있다.
// let으로 선언하면 그 변수는 선언하기 전에는 존재하지 않는다.

// 선언되지 않은 변수(에러 o) !== undefined 변수 (에러 x)

let foo
let bar = undefined

foo // undefined
bar // undefined
baz // ReferenceError baz is not defined

// 변수를 선언하지도 않았는데 그 변수에 접근할 수 있다는 특이한 현상이 발생

if (x !== 1) {
    console.log(y)  //undefined
    var y = 3
    if (y === 3) {
        var x = 1
    }
    console.log(y)  // 3
}
if (x === 1) {
    console.log(y)  // 3
}