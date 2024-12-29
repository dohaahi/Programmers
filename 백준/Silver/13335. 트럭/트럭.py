import sys

n, w, L = map(int, sys.stdin.readline().split())
trucks = list(map(int, sys.stdin.readline().split()))[::-1]

answer = 0

bridge = [0] * w


def move(bridge, new_truck):
    for i in range(1, w):
        bridge[w - i] = bridge[w - i - 1]
    bridge[0] = new_truck


while len(trucks) or any(bridge):
    if len(trucks) and sum(bridge) - bridge[-1] + trucks[-1] <= L:
        move(bridge, trucks.pop())
    else:
        move(bridge, 0)
    answer += 1

print(answer)
