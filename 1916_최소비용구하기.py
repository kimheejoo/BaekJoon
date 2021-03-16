import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
result = [sys.maxsize] * (N+1)
arr = {i+1:[] for i in range(N)}

for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    arr[u].append([v,w])

s , e = map(int, sys.stdin.readline().split())

queue = deque()
result[s] = 0
queue.append(s)

while queue:
    u = queue.popleft()
    for v, w in arr[u]:
        if result[v] > result[u] + w:
            result[v] = result[u] + w
            queue.append(v)

print(result[e])