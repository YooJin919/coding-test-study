# 단어 = 알파벳 소문자

# 1. 단어에서 임의의 2부분 골라서 단어 쪼개기 
  # (1개 단어 -> 3개 단어)
  # 적어도 길이가 1 이상의 단어
# 2. 3개 단어를 앞 뒤로 뒤집기
# 3. 원래 순서로 합치기

from sys import stdin

word = stdin.readline().rstrip()

history = []
for i in range(1, len(word)-1):
  for j in range(i+1, len(word)):
    a, b, c = word[:i], word[i:j], word[j:]
    a = ''.join(reversed(a))
    b = ''.join(reversed(b))
    c = ''.join(reversed(c))
    history.append(a+b+c)
    
print(sorted(history)[0])