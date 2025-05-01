# 거짓말을 했을 때 진실을 아는 사람 존재하면 -> 거짓말쟁이
# A 파티에서 진실, B 파티에서 거짓 -> 거짓말쟁이
# 거짓말쟁이가 아니면서 최대한 거짓말할 수 있는 파티 수 출력

# 진실 리스트 재구성 방법
  # 파티 구성원을 입력 받으면서 양방향 graph로 연결
  # 초기 입력받은 진실 리스트와 연결된 모든 구성원을 진실 리스트로 추가 (bfs)

from sys import stdin

res = 0
n, m = map(int, stdin.readline().split())

true = list(map(int, stdin.readline().split()))
truePeople = true[1:]

finalTruePeople = set(truePeople)
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

party = []
for _ in range(m):
  p = list(map(int, stdin.readline().split()))
  party.append(set(p[1:]))
  
  # 파티 멤버 그래프 연결
  for i in range(1, p[0]):
    for j in range(i+1, p[0] + 1):
      if p[i] not in graph[p[j]]:
        graph[p[i]].append(p[j])
        graph[p[j]].append(p[i])
  
# target과 연결된 모든 노드를 진실 리스트에 추가
def bfs(target):
  global finalTruePeople, graph, visited
  
  for node in graph[target]:
    if not visited[node]:
      finalTruePeople.add(node)
      visited[node] = True
      bfs(node)

for i in truePeople:
  bfs(i)

# 파티 멤버 중 진실을 아는 사람이 없을 때만 카운트
for members in party:
  if len(finalTruePeople & members) == 0:
    res += 1

print(res)