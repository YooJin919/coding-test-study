from sys import stdin

n = int(stdin.readline().rstrip())
arr = list(map(int, stdin.readline().split()))

sum = [arr[0]]

for i in range(1, n):
  sum.append(max(arr[i], arr[i] + sum[i-1]))
  
print(max(sum))