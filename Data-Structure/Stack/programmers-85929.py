def solution(s):
    stk = list()
    
    for p in s:
        if (p == "("):
            stk.append(p)
        elif (p == ")"):
            if (len(stk) > 0):
                cur = stk.pop()
            else:
                return False
    
    if(len(stk) == 0):
        return True
    else:
        return False
    