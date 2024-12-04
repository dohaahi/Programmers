import sys

money = int(sys.stdin.readline())

answer = 0

while money >= 2:
    if money % 5 == 0:
        answer += money // 5
        break

    money -= 2
    answer += 1

if answer > 0 and money != 1:
    print(answer)
else:
    print(-1)
