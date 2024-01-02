def solution(my_string):
    answer = [0] * 52

    for s in my_string:
        if s == s.upper():
            answer[ord(s) - ord('A')] += 1
        else:
            answer[ord(s) - ord('a') + 26] += 1

    return answer