function solution(n) {
    var sum = 0
    var num = String(n).split('').map((i) => {
        return i * 1
    })
    
    for(let i of num) {
        sum += i
    }
    return sum
}