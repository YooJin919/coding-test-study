from sys import stdin

N = int(stdin.readline().rstrip())
arr = [0 for _ in range(1000001)]
arr[1] = 0
arr[2] = 1
arr[3] = 1

def findMin(n):
  if(n % 6 == 0):
    arr[n] = min(arr[n//2], arr[n//3], arr[n-1]) + 1
  elif(n % 3 == 0 and arr[n//3] < arr[n-1]):
    arr[n] = arr[n//3] + 1
  elif(n % 2 == 0 and arr[n//2] < arr[n-1]):
    arr[n] = arr[n//2] + 1
  else:
    arr[n] = arr[n-1] + 1

if(N >= 4):
  for i in range(4, N+1):
    findMin(i)
print(arr[N])