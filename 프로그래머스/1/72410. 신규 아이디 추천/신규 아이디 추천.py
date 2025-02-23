import re


def solution(new_id):
    answer = ''

    # 1
    new_id = new_id.lower()

    # 2
    symbols = ['-', '_', '.']
    for n in new_id:
        if n.isalpha() or n.isnumeric() or n in symbols:
            answer += n

    # 3
    answer = re.sub(r'\.{1,}', '.',answer)

    # 4
    if len(answer) != 0:
        if answer[0] == '.':
            answer = answer[1:]
        if len(answer) != 0 and answer[-1] == '.':
            answer = answer[:len(answer) - 1]

    # 5
    if len(answer) == 0:
        answer = 'a'

    # 6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:14]

    # 7
    elif len(answer) <= 2:
        while len(answer) <= 2:
            answer += answer[-1]

    return answer
