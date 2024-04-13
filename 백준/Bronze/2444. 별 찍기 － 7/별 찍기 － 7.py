num = int(input())

for i in range(num):
    blank = ' ' * (num - i - 1)
    star = '*' * (2 * i + 1)
    print(blank + star)

for j in range(num - 1, 0, -1):
    blank = ' ' * (num - j)
    star = '*' * (2 * j - 1)
    print(blank + star)
