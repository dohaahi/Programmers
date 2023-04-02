function solution(my_string) {
    var low = my_string.toLowerCase().split('').sort().join('')
    return low;
}