str_list = []
answer = ""

for _ in range(5):
    str_list.append(input())

for i in range(15):
    for j in range(5):
        if i > len(str_list[j])-1:
            continue

        answer += str_list[j][i]

print(answer)