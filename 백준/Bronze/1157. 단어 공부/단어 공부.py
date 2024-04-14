str = input().upper()

set_str = set(str)

max_count = 0
answer = ''
for s in set_str:
    if str.count(s) == max_count:
        answer = '?'

    elif str.count(s) > max_count:
        max_count = str.count(s)
        answer = s

print(answer)
