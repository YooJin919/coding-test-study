def solution(i, j, k):
    answer = 0
    k = str(k)
    for n in range(i, j+1):
        answer += str(n).count(k)
    return answer