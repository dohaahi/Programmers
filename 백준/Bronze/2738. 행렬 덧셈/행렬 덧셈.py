n,m = map(int, input().split())

a, b = [], []
answer = []

for i in range(n * 2):
    if i < n:
        a.append(input().split())
    else:
        b.append(input().split())

for i in range(n):
    line = []
    for j in range(m):
        line.append(str(int(a[i][j]) + int(b[i][j])))
    answer.append(line)

for nn in answer:
    print(' '.join(nn))
