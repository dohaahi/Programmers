def solution(age):
    answer = ''
    for a in str(age):
        answer += chr(ord('a') + int(a))
    return answer