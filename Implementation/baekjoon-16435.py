# 과일을 먹으면 길이 1 증가
# 과일 : 지상에서 일정 높이에 존재 (i번째 과일의 높이 = h[i])
# 스네이크버드 길이보다 작거나 같은 과일을 먹을 수 있음

# 스네이크버드 길이가 L일 때, 과일을 먹어서 늘릴 수 있는 최대 길이 반환

from sys import stdin

n, l = map(int, stdin.readline().split())
h = list(map(int, stdin.readline().split()))

h.sort()

for hi in h:
  if hi <= l:
    l += 1
    
print(l)