def solution(strArr):
    my_dict = {}

    arr_map = list(map(lambda s: len(s), strArr))

    for i in arr_map:
        if my_dict.get(i) is not None:
            my_dict[i] += 1
            continue
        my_dict[i] = 1

    return max(sorted(my_dict.values(),  reverse=True))