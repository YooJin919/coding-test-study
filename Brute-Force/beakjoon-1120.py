# 길이 N 문자열 X, Y
# 두 문자열의 차이 = X[i] != Y[i] 개수

# A 길이 <= B 길이
# A 길이와 B 길이가 같아질 때까지 연산
# 1. A 앞에 아무 알파벳 추가
# 2. A 뒤에 아무 알파벳 추가

# A, B 길이 같으면서 차이가 최소로 만들기. 차이값 반환

from sys import stdin
from collections import deque

A, B = map(deque, stdin.readline().split())
min = 50

for startPoint in range(len(B) - len(A) + 1): # 0~3
  cnt = 0
  for i in range(len(A)):
    idx = startPoint + i
    if A[i] != B[idx]:
      cnt += 1
      
  if cnt < min:
    min = cnt
      
print(min)