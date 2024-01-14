from sys import stdin
from collections import deque

def dfs():
  if(len(stack) == M): # 조건 1 : M 길이에 맞는 수 출력 -> 길이가 M과 같으면 바로 종료
    print(' '.join(map(str,stack)))
    return
  for num in range(1, N+1):
    if(not visited[num]): # 조건 2 : 중복 불가 -> 방문여부 체크, 중복 아닌 경우만 탐색 진행
      stack.append(num)
      visited[num] = True
      dfs()
      stack.pop()
      visited[num] = False

N, M = map(int, stdin.readline().split())
stack = deque()
visited = [False] * (N+1)

dfs()