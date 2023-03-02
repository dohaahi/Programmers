function solution(array) {
    var answer = [...array];
    
    answer.sort((a,b) => b - a)
    let index = array.indexOf(answer[0])
    
    return [answer[0], index];
}