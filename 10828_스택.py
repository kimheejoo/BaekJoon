import sys
n = int(sys.stdin.readline())
stack = []

for i in range(n):
    tmp = sys.stdin.readline().split()
    if tmp[0] == "push":
        stack.append(tmp[1])
    elif tmp[0] == "pop":
        print(stack.pop()) if stack else print(-1)
    elif tmp[0] == "size":
        print(len(stack))
    elif tmp[0] == "empty":
        print(0) if stack else print(1)
    elif tmp[0] == "top":
        print(stack[-1]) if stack else print(-1)    

