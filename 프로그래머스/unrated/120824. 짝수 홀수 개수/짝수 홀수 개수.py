def solution(num_list):
    a = sum(1 for num in num_list if num % 2 == 0)
    return [a, len(num_list) - a]