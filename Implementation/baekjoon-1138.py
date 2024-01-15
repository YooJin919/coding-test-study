from sys import stdin

N = int(stdin.readline().rstrip())
human = list(map(int, stdin.readline().split()))
arr = [False for _ in range(N)]

for h, num in enumerate(human, start=1):
  cnt = 0
  for i in range(N):
    if(cnt == num):
      if(arr[i]):
        continue
      else:
        arr[i] = str(h)
      break
    elif(not arr[i]):
      cnt += 1

print(' '.join(arr))