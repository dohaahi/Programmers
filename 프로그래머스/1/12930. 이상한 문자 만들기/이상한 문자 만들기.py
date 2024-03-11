def solution(s):
    answer = []

    s = s.upper().split(' ')
    for ss in s:
        cen = ''
        for j in range(len(ss)):       
            if j % 2 != 0:
                cen+=ss[j].lower()
                continue
            cen+=ss[j]
        answer.append(cen)

    return ' '.join(answer)