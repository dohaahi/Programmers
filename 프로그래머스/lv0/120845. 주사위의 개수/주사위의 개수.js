function solution(box, n) {
    var answer = 1;
    
    for (length of box) {
        answer *= Math.trunc(length / n)
    }
    
    return answer;
}