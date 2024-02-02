def solution(A, B):
    count = 0

    result = list(B)
    my_str = list(A)
    while count < len(my_str):
        if my_str == result:
            return count
        
        count += 1
        last = my_str.pop()
        my_str.insert(0, last)

    return -1