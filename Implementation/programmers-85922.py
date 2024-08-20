def solution(array):
    answer = [0, 0]
    tmp = list(set(array))
    dup = False
    
    for t in tmp:
        n = array.count(t)
        if(n > answer[1]):
            answer = [t, n]
            dup = False
        elif(n == answer[1]):
            dup = True
    
    if(dup):
        return -1
    else:
        return answer[0]