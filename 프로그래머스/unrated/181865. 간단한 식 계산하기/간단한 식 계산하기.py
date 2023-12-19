def solution(binomial):
    split = binomial.split(' ')
    a = int(split[0])
    b = int(split[2])
    x = split[1]
    
    if x == '+':
        return  a + b
    elif x == '-':
        return a - b
    return a * b