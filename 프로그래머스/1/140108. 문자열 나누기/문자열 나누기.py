def solution(str):
    answer = 0

    target_str = str[0]
    target_count, none_target_count = 1, 0

    i, answer = 1, 1
    while i < len(str):
        while target_count != none_target_count or target_count == 0:
            if i == len(str) - 1:
                return answer

            if str[i] == target_str:
                target_count += 1

            else:
                none_target_count += 1
            i += 1

        target_count, none_target_count = 0, 0
        target_str = str[i]
        answer += 1

    return answer