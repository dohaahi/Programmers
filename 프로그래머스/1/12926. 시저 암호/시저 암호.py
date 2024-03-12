def solution(s, n):
    answer = ''

    for i in s:
        # 영어가 아닐 경우
        if not i.isalpha():
            answer += i
            continue

        # 영어 아스키 범위를 넘어간 경우
        if i.islower() and ord(i) + n > ord('z'):
            answer += chr(ord(i) - ord('z') + ord('a') + n-1)
        elif i.isupper() and ord(i) + n > ord('Z'):
            answer += chr(ord(i) - ord('Z') + ord('A') + n-1)

        else:
            answer += chr(ord(i) + n)

    return answer