function solution(hp) {
    var answer = 0;
    answer += parseInt(hp / 5)
    answer += parseInt((hp % 5) / 3)
    answer += parseInt((hp % 5) % 3)
    return answer;
}