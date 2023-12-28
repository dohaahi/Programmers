def solution(my_string):
    for s in my_string:
        if ord(s) >= ord('A'):
            my_string = my_string.replace(s, ' ')

    answer = my_string.split(' ')
    return sum(int(i) for i in answer if i != '')