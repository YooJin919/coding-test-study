def solution(participant, completion):
    d = {}
    
    for p in participant:
        if(p in d):
            d[p] += 1
        else:
            d[p] = 1
        
    for c in completion:
        if(c in d):
            d[c] -= 1
            if(d[c] == 0):
                del(d[c])
                
    return list(d)[0]