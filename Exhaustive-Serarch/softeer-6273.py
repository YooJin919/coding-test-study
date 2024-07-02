# 택배가 내려오는 레일 순서 조작 -> 최소의 무게
# N개 레일, Ni 무게 전용 레일 (같은 무게 없음)
# 레일 순서 정해지면 바구니 M 무게를 넘어가기 전에 옮겨야 함
# 레일 순서대로 택배 담기, M 무게 이하는 1번 일한 것
# K번 일하는데 최소 무게 출력

from sys import stdin
from  itertools import permutations

n, m, k = map(int, stdin.readline().split())
nList = list(map(int, stdin.readline().split()))
res = 9999999999

def calculateWeight(rail, limit, cnt):
  current = 0
  total = 0
  while(1):
    for weight in rail:
      if(current + weight > limit):
        cnt -= 1
        total += current
        current = weight
        if(cnt == 0):
          return total
      else:
        current += weight

  
for rail in permutations(nList, n):
  weight = calculateWeight(list(rail), m, k)

  if(res > weight):
    res = weight

print(res)