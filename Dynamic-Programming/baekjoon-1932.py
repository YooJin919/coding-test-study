# 삼각형 모양
# 크기 N = 한 변의 길이 N
# 꼭대기 -> 1층까지 갈 수 있는 경로 중 선택된 수의 최대 합 구하기

from sys import stdin

N = int(stdin.readline().rstrip())
triangle = []
sum = [[0] * N for _ in range(N)]

for _ in range(N):
  triangle.append(list(map(int, stdin.readline().split())))

sum[0][0] = triangle[0][0]
for i in range(1 ,N):
  for j in range(i+1):
    if j == 0: 
      sum[i][j] = sum[i-1][j]+triangle[i][j]
    else: 
      sum[i][j] = max(sum[i-1][j]+triangle[i][j], sum[i-1][j-1]+triangle[i][j])
    
print(max(sum[N-1]))