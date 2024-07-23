def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)
    realLost = list(lost-reserve)
    canReserve = list(reserve-lost)
    
    canReserve.sort()
    
    for r in canReserve:
        if (r-1 in realLost):
            realLost.pop(realLost.index(r-1))
        elif (r+1 in realLost):
            realLost.pop(realLost.index(r+1))
    
    return n - len(realLost)