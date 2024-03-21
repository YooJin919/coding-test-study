from sys import stdin
from itertools import permutations

N = int(stdin.readline().rstrip())
A = list(map(int, stdin.readline().split()))
max = 0
for arr in permutations(A, N):
  arr = list(arr)
  sum = 0
  for idx in range(N-1):
    sum += abs(arr[idx]-arr[idx+1])
  if(sum > max):
    max = sum
    
print(max)