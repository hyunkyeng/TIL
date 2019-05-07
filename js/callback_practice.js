// 배열로 이루어진 숫자들을 모두 더하는 함수
var numbers = [1, 2, 3, 4, 5,]
const numbersAddEach = numbers => {
    let sum = 0
    for (const number of numbers) {
        sum += number
    }
    return sum
}
numbersAddEach(numbers)
console.log(numbersAddEach(numbers))

// 배열로 이루어진 숫자들을 모두 빼는 함수

const numbersSubEach = numbers => {
    let sum = 0
    for (const number of numbers) {
        sum -= number
    }
    return sum
}
numbersSubEach(numbers)
console.log(numbersSubEach(numbers))

// 배열로 이루어진 숫자들을 모두 곱하는 함수

const numbersMulEach = numbers => {
    let sum = 1
    for (const number of numbers) {
        sum *= number
    }
    return sum
}
numbersMulEach(numbers)
console.log(numbersMulEach(numbers))