def solution(price, money, count):
    total = sum([price * (i + 1) for i in range(count)])
    return 0 if total < money else total - money