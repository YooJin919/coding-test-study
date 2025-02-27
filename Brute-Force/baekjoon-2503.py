from sys import stdin

questionCnt = int(stdin.readline().rstrip())

# 모든 후보군 생성
candidates = []
for i in range(1, 10):
  for j in range(1, 10):
    if i == j:
      continue
    for k in range(1, 10):
      if i == k or j == k:
        continue
      candidates.append(str(i) + str(j) + str(k))
      
# 질문마다 후보군 줄여나가기
for _ in range(questionCnt):
  number, strikeCnt, ballCnt = map(int, stdin.readline().split())
  tmp = []
  number = str(number)
  
  # 후보 숫자와 민혁이가 말한 수의 스트라이크, 볼 개수 비교
  for candidate in candidates:
    tmpStrikeCnt = 0
    tmpBallCnt = 0
    for i in range(3):
      if number[i] in candidate:
        if number[i] == candidate[i]:
          tmpStrikeCnt += 1
        else:
          tmpBallCnt += 1
    # 스트라이크, 볼 개수 동일한 수만 새로운 후보군으로 저장
    if tmpStrikeCnt == strikeCnt and tmpBallCnt == ballCnt:
      tmp.append(candidate)
  candidates = tmp

# 최종 후보군의 길이 출력
print(len(candidates))