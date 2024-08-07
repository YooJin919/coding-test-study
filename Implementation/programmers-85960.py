# 무기점 무기 구매
# 자신의 기사 번호의 약수 개수(3개, 4개)에 해당하는 공격력을 가진 무기를 구매
# 공격력 제한 수치보다 큰 무기를 구매할 경우, 협약기관에서 정한 공격력의 무기를 구매
# 전체 무기의 공격력 합 출력

import math

def getCnt(num):
    cnt = 2
    if (num == 1 or num == 2):
        return num
    for i in range(2, int(math.sqrt(num))+1):
        if (num % i == 0):
            cnt += 1
            if(num != i*i):
                cnt += 1
    return cnt

def solution(number, limit, power):
    answer = 0
    
    for n in range(1, number + 1):
        iron = getCnt(n)
        if(iron > limit):
            answer += power
        else:
            answer += iron
    
    return answer