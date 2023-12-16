def solution(num_list):
    a = num_list[-2]
    b = num_list[-1]

    if a < b:
        num_list.append(b - a)
        return num_list

    num_list.append(b * 2)
    return num_list