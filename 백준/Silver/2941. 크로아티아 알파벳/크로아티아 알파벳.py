str = input()

answer = 0

alp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for a in alp:
    if a in str:
        str = str.replace(a, 'C')

print(len(str))