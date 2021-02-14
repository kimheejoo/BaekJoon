import sys

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
result = [-1] * n
stack = []
for i in range(n):
    while(stack and arr[stack[-1]] < arr[i]):
        result[stack.pop()] = arr[i]
    stack.append(i)
print(*result)
# for i in range(n-1):
#     for j in range(i+1,n):
#         if arr[i] < arr[j]:
#             result[i] = arr[j]
#             break
# print(*result)
    

