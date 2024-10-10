# 독일 로또 : { 1 ~ 49 } 중 6개 수
# 가장 유명한 전략 : 49가지 수 중 k개 선택 (k > 6) -> 집합 S
# 집합 S의 수만 사용해서 번호를 선택

# 집합 S에서 6개의 수를 고를 수 있는 모든 경우의 수 출력 (조합)
# 사전 순으로 출력

# 라이브러리 사용하지 않기 !
# DFS + 재귀

from sys import stdin

def pickNumber(s, cnt, cur, res):
  if cnt == 6:
    print(' '.join(res))
    return

  for i in range(cur, len(s)):
    res[cnt] = str(s[i])
    pickNumber(s, cnt + 1, i + 1, res)

while(1):
  inputList = list(map(int, stdin.readline().split()))
  k = inputList[0]
  if k == 0:
    break
  s = inputList[1:]
  res = [0] * 6
  pickNumber(s, 0, 0, res)
  print()