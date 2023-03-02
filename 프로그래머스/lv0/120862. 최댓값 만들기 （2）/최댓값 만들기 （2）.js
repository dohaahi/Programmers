function solution(numbers) {
    var len = numbers.length
    
    numbers.sort((a,b) => a - b)
    if( numbers[0] * numbers[1] <= numbers[len-1]*numbers[len-2]) {
        return numbers[len-1]*numbers[len-2]
    } else {
        return numbers[0] * numbers[1]
    }

}