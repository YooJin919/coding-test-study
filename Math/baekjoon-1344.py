from sys import stdin
from math import comb
from math import pow

A = int(stdin.readline().rstrip()) / 100
B = int(stdin.readline().rstrip()) / 100
arr = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18]
pA = 0
pB = 0

for k in arr:
  pA += comb(18, k) * pow(A, k) * pow(1-A, 18-k)
  pB += comb(18, k) * pow(B, k) * pow(1-B, 18-k)

print(1-(pA*pB))
