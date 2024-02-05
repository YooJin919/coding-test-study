from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(10000)

# 인접한 지역 = 지렁이 1마리 -> 인접한 지역 개수 찾기 -> DFS

T = int(stdin.readline().rstrip())
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 인접한 배추 찾기
def dfs(y, x):    
    global visited
    global grid
    for i in range(4):
        yy = y + dy[i]
        xx = x + dx[i]
        if (0 <= yy < N) and (0 <= xx < M):
            if (grid[yy][xx] and not visited[yy][xx]):
                visited[yy][xx] = True
                dfs(yy, xx)

for _ in range(T):
    M, N, K = map(int, stdin.readline().split())
    grid = [[0 for _ in range(M)] for __ in range(N)]
    visited = [[False for _ in range(M)] for __ in range(N)]
    cnt = 0 # 인접한 배추 모임 개수 = 출력값
    
    # 배추 위치 입력받기
    for __ in range(K):
        X, Y = map(int, stdin.readline().split())
        grid[Y][X] = 1
        
    for i in range(M):
        for j in range(N):
            if (grid[j][i] and not visited[j][i]):
                visited[j][i] = True
                dfs(j, i)
                cnt += 1
    print(cnt)