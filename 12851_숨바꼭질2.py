import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

queue = deque()
visited = dict()
cnt = 0
min_sec = -1
queue.append((N,0))

while queue:
    now, now_sec = queue.popleft()
    visited[now] = 1
    
    if now_sec > min_sec and min_sec != -1:
        break
    if now == K: # 방법의 수
        if min_sec == -1: min_sec = now_sec
        cnt += 1
    
    if now - 1 not in visited and 0 <= now - 1 <= 100000:
        queue.append((now - 1, now_sec + 1))
    if now + 1 not in visited and 0 <= now + 1 <= 100000:
        queue.append((now + 1, now_sec + 1))
    if now * 2 not in visited and 0 <= now * 2 <= 100000:
        queue.append((now * 2, now_sec + 1))

print(min_sec)
print(cnt)