# 특정 프로세스가 몇 번째로 실행되는지
# 1. 대기 큐에서 프로세스 하나 pop
# 2. 방금 꺼낸 프로세스보다 우선순위가 높은 프로세스 있으면 다시 push
#    수가 크면 우선순위 높음
# 3. 없으면 실행

def checkPrio(q, cur):
    for now in q:
        if (cur[0] < now[0] and cur[1] != now[1]):
            return True

def solution(priorities, location):
    answer = 0
    queue = list()
    
    for i in range(len(priorities)):
        queue.append([priorities[i], i])
    
    while(queue):
        cur = queue.pop(0)
        if (checkPrio(queue, cur)):
            queue.append(cur)
            continue
        answer += 1
            
        if (cur[1] == location):
            return answer
        