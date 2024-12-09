import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split(' '))
q = list(map(int, sys.stdin.readline().split(' ')))

d_num = deque([i for i in range(1, n + 1)])
answer = 0

for n in q:
    if d_num.index(n) <= len(d_num) // 2:
        while d_num[0] != n:
            answer += 1
            d_num.append(d_num.popleft())
    else:
        while d_num[0] != n:
            answer += 1
            d_num.appendleft(d_num.pop())
    d_num.popleft()

print(answer)
