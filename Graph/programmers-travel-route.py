def solution(tickets):
    answer = []
    route = dict()
    
    # 출발지, 목적지 저장
    for ticket in tickets:
        if(ticket[0] in route):
            route[ticket[0]].append(ticket[1])
        else:
            route[ticket[0]] = list()
            route[ticket[0]].append(ticket[1])
    
    # 목적지 정렬
    for k in route.keys():
        route[k].sort(reverse=True)
        
    stk = list()
    stk.append("ICN")
    
    while(stk):
        now = stk[-1]
        if(now not in route or len(route[now]) == 0):
            answer.append(stk.pop())
        else:
            stk.append(route[now].pop())
    
    return answer[::-1]