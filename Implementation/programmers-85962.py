# 하나의 키에 여러 문자 할당
# 동일한 키를 여러 번 누르면 문자 바뀜
# 1 <= 자판키 <= 100
# 최소로 누르는 횟수

def solution(keymap, targets):
    answer = []
    minCnt = {}
    tmp = list(set(list(''.join(keymap))))
    
    for t in tmp:
        if (t not in minCnt):
            minCnt[t] = 999
        
        for key in keymap:
            cnt = 0
            for k in key:
                cnt += 1
                if (t == k and cnt < minCnt[t]):
                    minCnt[t] = cnt
                    break
    
    for target in targets:
        cnt = 0
        cant = False
        for t in target:
            if(t not in minCnt):
                answer.append(-1)
                cant = True
                break
            cnt += minCnt[t]
        if (not cant):
            answer.append(cnt)
    
    return answer