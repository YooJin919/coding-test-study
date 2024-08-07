# 야근하면 피로도 쌓임
# 야근 피로도 += 야근 시작 시점에서 남은 작업량 제곱
# N시간 동안 야근 피로도를 최소화하도록 일할거임
# 1시간 동안 작업량 1만큼 처리
# 퇴근까지 남은 시간과 일의 작업량에 대해 야근 피로도를 최소화한 값을 반환

import heapq
from copy import deepcopy

def solution(n, works):
    answer = 0
    h = []
    for i in works:
        heapq.heappush(h, -i)
    
    for i in range(n):
        if(len(h) == 0):
            continue
        num = heapq.heappop(h)
        if(num+1 == 0):
            continue
        heapq.heappush(h, num+1)
        
    for n in h:
        answer += (-n)**2
    
    return answer