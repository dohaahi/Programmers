def solution(babbling):
    answer = 0
    ong = ["aya", "ye", "woo", "ma"]

    for b in babbling:
        s = b
        count = 0
        for o in ong:
            if s == "":
                break
            if o in s and o * 2 not in s:
                count += s.count(o)
                s = s.replace(o, "-")
                continue

        if s == "-" * count:
            answer += 1

    return answer