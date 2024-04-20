def solution(n, m):
    answer = [1, 1]

    nn = get_num(n)
    mm = get_num(m)
    common = set(nn + mm)

    # 최소공배수
    for c_num in common:
        min_count = min(nn.count(c_num), mm.count(c_num))
        answer[0] *= pow(c_num, min_count) if min_count != 0 else 1
    answer[1] = (n * m) // answer[0]

    return answer


def get_num(n):
    primary_num = []
    share = 2

    div_num = n
    while div_num != 1:
        if div_num % share == 0:
            div_num //= share
            primary_num.append(share)
        else:
            share += 1

    return primary_num