function solution(numbers) {
    var newNum = numbers.sort((a,b) => a-b)
    let len = newNum.length
    return newNum[len-1] * newNum[len-2];
}