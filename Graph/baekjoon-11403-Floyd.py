# Floyd-Warshall 208ms
from sys import stdin

# 입력 받기
N = int(stdin.readline().rstrip())
graph = []
for _ in range(N):
  graph.append(stdin.readline().split())
  
for i in range(N):
    for j in range(N):
        for k in range(N):
            if graph[j][i] == "1" and graph[i][k] == "1":
                graph[j][k] = "1"
                
for _ in graph:
    print(' '.join(_))