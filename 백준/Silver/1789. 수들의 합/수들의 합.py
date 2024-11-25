s = int(input())

for n in range(4294967295 ** 2):
    if n * (n + 1) > 2 * s:
        print(n - 1)
        break