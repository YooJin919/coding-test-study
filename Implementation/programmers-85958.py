def solution(n, m, section):
    answer = 0
    start = section[0]
    
    for s in section:
        if(start <= s):
            answer += 1
            start = s + m
    
    return answer
