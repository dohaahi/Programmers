function solution(num_list) {
    var result = num_list.filter(number => number % 2 == 0)
    return [result.length, num_list.length-result.length];
}