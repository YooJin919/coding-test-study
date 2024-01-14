import sys
from itertools import combinations

memberNum = int(input())
member = list(range(memberNum))
abilityScore = []
minDiff = 999

# 능력치 입력받기
for _ in range(memberNum):
  abilityScore.append(list(map(int, sys.stdin.readline().split())))

# 2개 팀으로 나누기 (조합)
for team1 in combinations(member, memberNum//2):
  team2 = tuple(set(member)-set(team1))
  ability1 = 0
  ability2 = 0
  # 각 팀별 능력치 합산
  for t1 in combinations(team1, 2):
    ability1 += abilityScore[t1[0]][t1[1]] + abilityScore[t1[1]][t1[0]]
  for t2 in combinations(team2, 2):
    ability2 += abilityScore[t2[0]][t2[1]] + abilityScore[t2[1]][t2[0]]
  
  # 최소 능력치 비교
  currentDiff = abs(ability1-ability2)
  if(currentDiff < minDiff):
    minDiff = currentDiff
    
print(minDiff)
  