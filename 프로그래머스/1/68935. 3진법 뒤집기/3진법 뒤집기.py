def solution(n):
    num = ''
    answer = 0

    while n > 0:
        a, b = divmod(n, 3)
        n = a
        num += str(b)
    num = num[::-1]

    for i in range(len(num)):
        answer += int(num[i]) * pow(3, i)

    return answer