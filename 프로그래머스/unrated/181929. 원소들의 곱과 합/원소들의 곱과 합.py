def solution(num_list):
    a = 1
    
    for n in num_list:
        a *= n
        
    b = sum(n for n in num_list) ** 2
    
    if a < b:
        return 1

    return 0