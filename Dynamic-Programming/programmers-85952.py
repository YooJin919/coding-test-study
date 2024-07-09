def solution(N, number):
    num = [set() for x in range(8)] 
    
    for i in range(8):
        num[i].add(int(str(N)*(i+1)))
        
    for i in range(len(num)): 
        for j in range(i): 
            for op1 in num[j]:
                for op2 in num[i-j-1]:
                    num[i].add(op1 + op2)
                    num[i].add(op1 - op2)
                    num[i].add(op1 * op2)
                    if op2 != 0:
                        num[i].add(op1 // op2)
                        
        if number in num[i]: 
            answer = i + 1
            break
        else:
            answer = -1
            
    return answer