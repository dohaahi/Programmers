def solution(clothes):
    answer = 1

    cloth_dict = {}

    # clothes 돌면서 의상 종류 뽑기
    for v, k in clothes:
        if k in cloth_dict.keys():
            cloth_dict[k].append(v)
        else:
            cloth_dict[k] = list([v])

    for v in cloth_dict.values():
        answer *= len(v) + 1

    return answer - 1
