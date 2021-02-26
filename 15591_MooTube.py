import sys

# graph = [정점 번호, 거리]
def search(k, node):
    result = 0
    visited = [False] * (len(graph.keys())+1)
    stack = graph[node][:]
    visited[node] = True

    # 정점과 인접해있는 노드에서 k이상이면 result++
    for s in stack: 
        visited[s[0]] = True
        if s[1] >= k:
            result += 1

    # 인접해있는 노드말고
    while stack:
        n, d = stack.pop()
        min_d = d
        for i in graph[n]:
            if not visited[i[0]]:
                visited[i[0]] = True
                min_d = min(d, i[1])
                stack.append([i[0], min(d, i[1])])
                if min_d >= k:
                    result += 1
    return result

n, q = map(int, sys.stdin.readline().split())
graph = dict()
for i in range(n-1):
    tmp = list(map(int, sys.stdin.readline().split()))
    if not graph.get(tmp[0]):
        graph[tmp[0]] = list()
    if not graph.get(tmp[1]):
        graph[tmp[1]] = list()
    graph[tmp[0]].append([tmp[1], tmp[2]])
    graph[tmp[1]].append([tmp[0], tmp[2]])

for i in range(q):
    tmp = list(map(int, sys.stdin.readline().split()))
    print(search(tmp[0],tmp[1]))
