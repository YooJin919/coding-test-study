# 자연수 카드 n장
# i번 카드 = ai

# 카드 합체 과정 (m번 반복 후 n장 카드 수 합 = 놀이의 점수)
# 1. x번 카드 + y번 카드
# 2. x번 카드, y번 카드 값을 1번 값으로 변경

# 가능한 가장 작은 놀이 점수 반환

from sys import stdin

n, m = map(int, stdin.readline().split())
card = list(map(int, stdin.readline().split()))

for _ in range(m):
  card.sort()
  card[0], card[1] = card[0]+card[1], card[0]+card[1]
  
print(sum(card))