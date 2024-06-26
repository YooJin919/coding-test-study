import sys

# n*n 정원 나무 정리
# 4번 인접해 있는 두 나무 묶기
# 묶은 나무 겹치지 않음
# 두 나무가 묵였을 때 묶인 2개 나무 키 합의 최대

garden = []
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    garden.append(list(map(int, sys.stdin.readline().split())))

visited = [[False] * n for _ in range(n)]
res = 0


move = [[-1, 0], [0, 1]] # 오른쪽, 아래 -> 2방향만 확인

def dfs(i, j, cnt, totalSum):
    global res, visited, garden
    
    visited[i][j] = True

    # 현재 위치에서 오른쪽, 아래 묶기 가능한지 확인
    for mi, mj in move:
        nowI = i + mi
        nowJ = j + mj
        
        if(0 <= nowI < n and 0 <= nowJ < n and not visited[nowI][nowJ]):
            tmpSum = totalSum + garden[i][j] + garden[nowI][nowJ]
            visited[nowI][nowJ] = True

            # 현재까지 4묶음 완성 -> 최대 값 비교
            if(cnt == 3 or (n < 3 and cnt == 1)): 
                res = max(res, tmpSum)
                visited[nowI][nowJ] = False
                return 

            # 추가로 묶을 나무 찾기
            for x in range(n):
                for y in range(n):
                    if(not visited[x][y]):
                        dfs(x, y, cnt+1, tmpSum)
                        visited[x][y] = False
                        
            visited[nowI][nowJ] = False


# 첫 번째 그룹 시작 지점 찾기
for x in range(n):
    for y in range(n):
        if(not visited[x][y]):
            visited[x][y] = True
            dfs(x, y, 0, 0) # i / j / 묶은 그룹 개수 / 묶은 그룹 height 합
            visited[x][y] = False

print(res)