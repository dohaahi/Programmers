def solution(num_list, n):
    return num_list[n:].__add__(num_list[:n])