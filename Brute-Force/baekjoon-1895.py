# 정렬된 숫자 9개, 중앙값 = 5번째 숫자 (n/2) 올림

# 이미지 I = 크기 (R X C), 값 = 어두운 정도 V
# 중앙 필터 : 노이즈 제거 필터 (3 X 3)
# 이미지의 중앙값을 찾으면 노이즈 제거

from sys import stdin

r, c = map(int, stdin.readline().split())
image = []
mid = []
res = 0

for _ in range(r):
  image.append(list(map(int, stdin.readline().split())))
t = int(stdin.readline().rstrip())


for i in range(r - 2):
  for j in range(c - 2):
    for f in range(3):
      mid += image[i+f][j:j+3]
    mid.sort()
    if mid[4] >= t:
      res += 1
    mid = []
    
print(res)