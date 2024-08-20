def solution(array):
    answer = [array[0], 0]
    
    for i in range(len(array)):
        if(array[i] > answer[0]):
            answer = [array[i], i]
    
    return answer