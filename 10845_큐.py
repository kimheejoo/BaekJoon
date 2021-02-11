from collections import deque
import sys

n = int(sys.stdin.readline())
queue = deque()

for i in range(n):
    tmp = sys.stdin.readline().split()
    if tmp[0] == 'push':
        queue.append(tmp[1])
    elif tmp[0] == 'pop':
        print(queue.popleft()) if queue else print(-1)
    elif tmp[0] == 'size':
        print(len(queue))
    elif tmp[0] == 'empty':
        print(0) if queue else print(1)
    elif tmp[0] == 'front':
        print(queue[0]) if queue else print(-1)
    elif tmp[0] == 'back':
        print(queue[-1]) if queue else print(-1)