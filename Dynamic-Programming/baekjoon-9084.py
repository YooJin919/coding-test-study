# 주어진 동전 가지 수를 중복 가능하게 활용하여 목표 금액을 만들 수 있는 경우의 수 출력

from sys import stdin

T = int(stdin.readline().rstrip())
for _ in range(T):
  N = int(stdin.readline().rstrip()) # 동전 가지 수
  coinType = [0]
  coinType += list(map(int, stdin.readline().split())) # 동전 금액
  M = int(stdin.readline().rstrip()) # 목표 금액
  caseCnt = [[0] * (N+1) for _ in range(M+1)]
  caseCnt[0][0] = 1
  
  for i in range(1, N+1):
    for m in range(M+1):
      if m % coinType[i] == 0:
        caseCnt[m][i] = 1
  
  for i in range(1, N+1): # 동전 타입 idx
    for m in range(M+1): # 현재 금액
      if m < coinType[i]:
        caseCnt[m][i] = caseCnt[m][i-1]
      else:
        caseCnt[m][i] = caseCnt[m-coinType[i]][i] + caseCnt[m][i-1]
  
  print(caseCnt[M][N])
  