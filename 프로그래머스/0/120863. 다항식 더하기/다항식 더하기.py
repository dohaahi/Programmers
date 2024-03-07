def solution(polynomial):
    nums = polynomial.split(' + ')
    x = 0
    n = 0

    for num in nums:
        if num == 'x':
            x += 1
        elif 'x' in num:
            x += int(str.replace(num, 'x', ''))
        else:
            n += int(num)
            
    if x == 1:
        x = ''

    if x != 0 and n != 0:
        return str(x) + 'x + ' + str(n)
    elif x != 0:
        return str(x) +'x'
    return str(n)