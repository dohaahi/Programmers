function solution(my_string) {
    var sum = 0
    var answer = my_string.split('').filter(i=>!isNaN(i)).map(i=>{
        sum += parseInt(i)
    })
    return sum;
}