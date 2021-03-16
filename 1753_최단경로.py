import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
INF = sys.maxsize
graph = [INF] * (V+1)
queue = []
arr = {i+1:[] for i in range(V)}

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    arr[u].append([v, w])

heapq.heappush(queue, [0, start])
graph[start] = 0

while queue:
    w, now = heapq.heappop(queue)
    for i in arr[now]:
        if graph[i[0]] > w+i[1]:
            graph[i[0]] = w+i[1]
            heapq.heappush(queue, [graph[i[0]], i[0]])

for i in range(1, V+1):
    print(graph[i] if graph[i]!=INF else 'INF')