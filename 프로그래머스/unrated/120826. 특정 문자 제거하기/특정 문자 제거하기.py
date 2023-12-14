def solution(my_string, letter):
    answer = ''
    
    for str in my_string:
        if str == letter:
            continue
        else:
            answer += str
            
    return answer