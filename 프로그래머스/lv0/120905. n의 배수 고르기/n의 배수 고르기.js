function solution(n, numlist) {
    var answer = numlist.filter(i => {
        return i % n == 0
    })
    return answer;
}