import sys

n, m = map(int, sys.stdin.readline().split())

floor = []

for i in range(int(n)):
    floor.append(sys.stdin.readline().strip())

count = n * m
for i in range(n):
    for j in range(m):
        # "-" 타일일 경우
        if floor[i][j] == "-":
            # 옆 타일이 "-"라면 count--
            if j + 1 < m and floor[i][j + 1] == "-":
                count = count - 1
        # "|" 타일일 경우
        else:
            # 밑 타일이 "|"라면 count--
            if i + 1 < n and floor[i + 1][j] == "|":
                count = count - 1

print(count)
