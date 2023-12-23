def solution(num_list, n):
    answer = []

    for i in range(0,len(num_list),n):
        listt = []
        for j in range(i,i+n):
            listt.append(num_list[j])
        answer.append( listt)

    return answer