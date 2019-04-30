var _ = require('lodash');
let list = ['짜장면', '짬뽕', '볶음밥',]
let numbers = _.range(1, 46)
let lottery = _.sampleSize(numbers, 6)
let pick = _.sample(list)
let menu = {
    짜장면: 'http://cdnweb01.wikitree.co.kr/webdata/editor/201704/13/img_20170413122520_54eea70d.jpg',
    짬뽕: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1Qlr0I7HBilvlPuiKQS1Eob2PPBLOGKwmypOj696g8O373vZvFw',
    볶음밥: 'https://t1.daumcdn.net/cfile/tistory/136532424F08529921',

}

console.log(`오늘의 메뉴는 ${pick}입니다.`)
console.log(menu[pick])
console.log(`행운의 번호: ${lottery}`)

let getMin = (a, b) => {
    if (a > b) {
        return b
    }
    return a
}


let getMinFromArray = nums => {
    let min = Infinity      // 양의 무한대, 다른 어떤 수보다 더 큼
    // nums 배경을 돌면서 min 변수와 비교하여 최소값을 찾는다
    for (num of nums) {
        if (min > num) {
            min = num
        }
    }
    return min
}
ssafy = [1, 2, 3, 4, 5,]
console.log(getMinFromArray(ssafy))