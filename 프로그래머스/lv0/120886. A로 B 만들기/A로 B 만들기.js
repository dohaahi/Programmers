function solution(before, after) {
    var before_string = before.split('').sort().join('')
    var after_string = after.split('').sort().join('')
    return before_string == after_string? 1 : 0
}