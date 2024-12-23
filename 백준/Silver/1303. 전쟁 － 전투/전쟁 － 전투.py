import sys

N, M = map(int, sys.stdin.readline().split())
data = [sys.stdin.readline().rstrip() for _ in range(M)]

visited = [[False] * N for _ in range(M)]
answer = [0, 0]  # [W,B]


def dfs(x, y, pre_color):
    visited[x][y] = True
    count = 1

    direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and data[nx][ny] == pre_color:
            count += dfs(nx, ny, pre_color)

    return count


for x in range(M):
    for y in range(N):
        if not visited[x][y]:
            color = data[x][y]
            power = dfs(x, y, color) ** 2

            if color == 'W':
                answer[0] += power
            else:
                answer[1] += power

print(answer[0], answer[1])
