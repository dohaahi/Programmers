def solution(myStr):
    answer = []

    my_string = ''
    for s in myStr:
        if (s == 'a' or s == 'b' or s == 'c'):
            if my_string != '':
                answer.append(my_string)
                my_string = ''
            continue
        my_string += s
    answer.append(my_string)

    return answer if answer[0] != '' else ['EMPTY']