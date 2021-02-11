import sys

n = int(sys.stdin.readline())
stack = []

for i in range(n):
    tmp = int(sys.stdin.readline())
    if tmp!=0:
        stack.append(tmp)
    else:
        stack.pop()
print(sum(stack))
