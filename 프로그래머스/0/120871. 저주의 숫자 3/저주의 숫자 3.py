def solution(n):
    new_n = 1
    
    for i in range(n):
        while '3' in str(new_n) or new_n % 3 == 0:
            new_n += 1
        new_n += 1

    return new_n -1