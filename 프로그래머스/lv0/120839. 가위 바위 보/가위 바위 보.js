function solution(rsp) {
    var answer = rsp.split('')
    var result = ''
    
    for(let i of answer) {
        if(i == 2) {
            result += 0
        } else if (i == 0) {
            result += 5
        } else {
            result += 2
        }
    }
    return result;
}