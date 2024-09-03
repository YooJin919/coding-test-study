def solution(n, s):
    answer = []
    
    if s/n < 1:
        return [-1]
    
    answer = [s//n] * n
    
    if s > (s//n)*n:
        cnt = s - (s//n)*n
        for i in range(n-1, n-1-cnt, -1):
            answer[i] += 1
    
    return answer