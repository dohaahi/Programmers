import sys

l = int(sys.stdin.readline())

graph = []
for i in range(l):
    graph.append(sys.stdin.readline().strip())

answer = ''

for g in graph:
    stack = []
    for s in g:
        if s == ')' and '(' in stack:
            stack.pop()
        elif s == '(':
            stack.append('(')
        elif s == ')':
            stack.append(')')

    if len(stack) != 0:
        answer += 'NO\n'
    else:
        answer += 'YES\n'

print(answer)