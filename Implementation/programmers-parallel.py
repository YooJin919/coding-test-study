from itertools import combinations
def solution(dots):
    combList = list(combinations(dots, 2))
    
    for i in range(3):
        dot1, dot2 = combList[i]
        dot3, dot4 = combList[5-i]
        
        if((dot2[1]-dot1[1])/(dot2[0]-dot1[0]) == (dot4[1]-dot3[1])/(dot4[0]-dot3[0])):
            return 1
        
    
    return 0