from sys import stdin

# -를 기준으로 자르기
exp = stdin.readline().rstrip().split("-")
arr = []

# 각 요소 합구하기
for n in exp:
  arr.append(sum(list(map(int, n.split("+")))))
  
# 배열 앞에서부터 "-" 연산
res = arr[0]
for idx in range(1, len(arr)):
  res -= arr[idx]
  
print(res)