function solution(num, k) {
    var number = String(num)
    
    if(!(String(num).indexOf(k) +1)) {
        return -1
    }
    return String(num).indexOf(k) +1;
}