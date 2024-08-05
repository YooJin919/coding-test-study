def solution(array):
    answer = 0
    for n in array:
        n = str(n)
        answer += n.count("7")
    return answer