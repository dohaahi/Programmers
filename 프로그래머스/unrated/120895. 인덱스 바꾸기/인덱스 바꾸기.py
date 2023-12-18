def solution(my_string, num1, num2):
    answer = ''
    
    next = ''
    for i in range(len(my_string)):
        if i == num1:        
            next = my_string[i]
            answer += my_string[num2]
            continue
        elif i == num2:
            answer += next
            continue
        answer += my_string[i]
            
    return answer