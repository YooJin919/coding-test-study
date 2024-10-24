# 고속도로 센서 N개
# 센서에서 자료를 받을 집중국 세우기
# 최대 K개 집중국 설치 가능
# 집중국 : 센서의 수신 가능 영역 조절 가능 / 집중국의 수신 가능 영역 == 고속도로 상 연결된 구간

# N개의 센서가 적어도 1개의 집중국과 통신 가능해야 함
# 각 집중국의 수신 가능 영역의 길이의 합이 최소

# 고속도로 : 직선
# 센서 : 직선 위의 한 기점인 원점에서 정수 거리에 위치
# 센서의 좌표 : 정수 하나 (0, X) -> -1,000,000 <= X <= 1,000,000

from sys import stdin

n = int(stdin.readline().rstrip())
k = int(stdin.readline().rstrip())
sensorList = list(map(int, stdin.readline().split()))
res = 0

sensorList.sort()
dis = []
for i in range(n-1):
  dis.append(sensorList[i+1] - sensorList[i])
  
dis.sort()
res = sum(dis[:n-k])
print(res)
  