# 한 번에 한 명 신고
# 신고 횟수 제한 없음
# 한 유저 여러 번 신고 가능하지만 1회로 처리
# k번 이상 신고된 유저 정지, 신고한 유저에게 메일 발송
# 각 유저별 메일 받은 횟수 반환

def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    cnt = {}
    who = {}
    stop = []
    
    for name in id_list:
        cnt[name] = 0
        who[name] = []
    
    report = list(set(report))
    
    for r in report:
        a, b = r.split()
        cnt[b] += 1
        who[b].append(a)
    
    for name in id_list:
        if(cnt[name] >= k):
            stop.append(name)
    
    for idx in range(len(id_list)):
        tmp = 0
        for s in stop:
            if(id_list[idx] in who[s]):
                tmp += 1
        answer[idx] = tmp
        
    return answer