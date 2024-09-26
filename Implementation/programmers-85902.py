def solution(order):
    answer = 0
    order = str(order)
    
    for i in ["3", "6", "9"]:
        answer += order.count(i)
    
    return answer