import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

for i in range(T):
  arr = deque(sys.stdin.readline().rstrip())
  stack = deque()
  for p in arr:
    if(p == "("):
      stack.append(p)
    elif(p == ")"):
      if(len(stack) == 0):
        stack.append("NO")
        break
      stack.pop()
  
  if(len(stack) == 0):
    print("YES")
  else:
    print("NO")