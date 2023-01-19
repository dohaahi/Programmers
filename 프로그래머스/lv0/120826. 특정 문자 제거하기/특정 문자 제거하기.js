function solution(my_string, letter) {
    var answer = my_string.split('').filter(i=>(i !== letter)).join('');
    return answer;
}