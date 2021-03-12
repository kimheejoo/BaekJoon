import sys

def DFS(w, h, i, j, arr):
    if i>=h or j>=w or arr[i][j]==0:
        return
    
    if arr[i][j]==1:
        DFS(w, h, i, j+1, arr)
        DFS(w, h ,i+1, j, arr)
        DFS(w, h, i+1, j+1, arr)
        arr[i][j] = 0


while True:
    w, h = map(int, sys.stdin.readline().split())
    if w * h == 0:
        break
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    print(DFS(w, h , 0, 0, arr))