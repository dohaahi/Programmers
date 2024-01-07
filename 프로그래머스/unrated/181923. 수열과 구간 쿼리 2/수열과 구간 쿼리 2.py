def solution(arr, queries):
    answer = []

    for s, e, k in queries:
        new_arr = sorted(arr[s:e + 1])
        list = []
        for q in new_arr:
            if q > k:
                list.append(q)
                
        answer.append(-1) if not list else answer.append(min(list))

    return answer