# N명 회원 치킨 주문
# M가지 종류 치킨
# 회원마다 치킨 선호도 존재
# 한 사람의 만족도 = 시킨 치킨 중 선호도가 가장 큰 값
# 회원들의 만족도 합이 최대가 되도록 치킨 시키려고 함
# 3가지 종류 치킨 주문
# 가능한 만족도 합의 최댓값 반환

from sys import stdin
from itertools import combinations

n, m = map(int, stdin.readline().split())
preference = []
res = 0
for _ in range(n):
  preference.append(list(map(int, stdin.readline().split())))

combinationList = list(map(list, combinations(range(m), 3)))

for comb in combinationList:
  cur = 0
  for i in range(n):
    cur += max(preference[i][comb[0]], preference[i][comb[1]], preference[i][comb[2]])
  if cur > res:
    res = cur

print(res)