import sys

value = sys.stdin.readline().strip()


def method():
    answer = ''

    if value[0].isupper() or value[0] == '_' or value[-1] == '_' or len(value) == 0:
        return "Error!"

    if '_' in value:
        i = 0
        while i < len(value):
            temp = value[i]
            if temp == '_':
                if i + 1 >= len(value) or value[i + 1].isupper() or value[i + 1] == '_':
                    return "Error!"
                answer += value[i + 1].upper()
                i += 1
            else:
                if temp.isupper():
                    return "Error!"
                answer += temp
            i += 1
    else:
        for v in value:
            if v.isupper():
                answer += '_' + v.lower()
            else:
                answer += v

    return answer


print(method())

# 밑줄이 두개 연속
# 마지막이 밑줄 & 시작이 밑줄
# 대문자로 시작
# 대문자 + 밑줄
