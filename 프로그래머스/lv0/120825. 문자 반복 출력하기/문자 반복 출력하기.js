function solution(my_string, n) {
    my_string = my_string.split('')
    var result = my_string.map((i) => {
        return i.repeat(n)
    })
    return result.join('')
}