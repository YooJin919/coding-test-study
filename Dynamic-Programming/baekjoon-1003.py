import sys

T = int(sys.stdin.readline().rstrip())
arr = [[0, 0] for _ in range(41)]
arr[0] = [1, 0]
arr[1] = [0, 1]

for _ in range(T):
  N = int(sys.stdin.readline().rstrip())
  for i in range(2, N+1):
    if(arr[i][0] != 0 or arr[i][1] != 0):
      continue
    arr[i][0] = arr[i-1][0]+arr[i-2][0]
    arr[i][1] = arr[i-1][1]+arr[i-2][1]
  print(arr[N][0], arr[N][1])