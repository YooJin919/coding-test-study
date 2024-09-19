# 두 수의 짝꿍 = 두 정수의 임의의 자리에서 공통으로 나타나는 정수 k를 이용해서 만들 수 있는 가장 큰 정수
# 짝꿍이 존재하지 않으면 -1, 두 정수가 0이면 짝꿍은 0

def solution(X, Y):
    answer = ''
    
    for i in range(9, -1, -1):
        i = str(i)
        n1 = X.count(i)
        n2 = Y.count(i)
        
        if(n1 < n2):
            answer += i*n1
        else:
            answer += i*n2
            
    if(answer == ''):
        return '-1'
    elif(answer.count('0') == len(answer)):
        return '0'
    return answer