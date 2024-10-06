# 국회의원 후보 N명, 다솜이는 항상 1번
# 자신을 찍지 않는 사람을 돈으로 매수 -> 국회의원 당선 목표
# 당선 기준 = 다른 모든 사람의 득표수보다 많은 득표수를 가질 때
# 돈으로 매수해야하는 사람의 최솟값 출력

from sys import stdin

res = 0
n = int(stdin.readline().rstrip())
vote = []

for _ in range(n):
  voteNum = int(stdin.readline().rstrip())
  vote.append(voteNum)

ds = vote[0]
vote = vote[1:]

if n == 1:
  print(0)
else:
  while(1):
    if ds > max(vote):
      break
    for cmp in vote:
      if ds <= cmp:
        break
    j = vote.index(max(vote))
    vote[j] -= 1
    ds += 1
    res += 1

  print(res)