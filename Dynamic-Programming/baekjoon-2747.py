import sys

n = int(sys.stdin.readline().rstrip())
arr = [0 for _ in range(n+1)]

arr[0], arr[1] = 0, 1

for idx in range(2, n+1):
  arr[idx] = arr[idx-1] + arr[idx-2]
  
print(arr[n])