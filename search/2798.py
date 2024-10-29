import sys
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
result = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1,n):
            if arr[i] + arr[j] + arr[k] > m:
                continue
            else:
                result = max(result, arr[i] + arr[j] + arr[k])
                
print(result)