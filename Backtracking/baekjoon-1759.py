from sys import stdin
from collections import deque

l, c = map(int, stdin.readline().split())
alphabet = stdin.readline().split()
alphabet = sorted(alphabet)
used = {}
str1, str2 = 0, 0

def dfs(depth, pw):
  global str1, str2
  if(depth == l and str1 >= 1 and str2 >= 2):
    print(pw)
    return
  for s in alphabet:
    if(not used.get(s)):
      if(depth==0 or pw[-1] < s): # 오름차순만 받기
        if(s in ['a', 'e', 'i', 'o', 'u']):
          str1 += 1
        else:
          str2 += 1
        used[s] = True
        dfs(depth+1, pw+s)
        if(s in ['a', 'e', 'i', 'o', 'u']):
          str1 -= 1
        else:
          str2 -= 1
        used[s] = False
      
dfs(0, "")