# 모든 음식의 맵기 K 이상
# 첫 번째 최소 맵기 + 두 번째 최소 맵기 * 2

import heapq

def solution(s, K):
    answer = 0
    heapq.heapify(s)
    
    while(s[0] < K):
        min1 = heapq.heappop(s)
        min2 = heapq.heappop(s)
        heapq.heappush(s, min1+min2*2)
        answer += 1
        
        if(len(s) < 2 and s[0] < K):
            return -1
    
    return answer