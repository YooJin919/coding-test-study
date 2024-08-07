def solution(survey, choices):
    answer = ''
    score = {1:[0,3], 2:[0,2], 3:[0,1], 4:[0,0], 5:[1,1], 6:[1,2], 7:[1,3]}
    res = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    pair = [["R", "T"], ["C", "F"], ["J", "M"], ["A", "N"]]
    
    for idx in range(len(survey)):
        c = choices[idx]
        
        target = score[c][0]
        num = score[c][1]
        res[survey[idx][target]] += num
        
    for p in pair:
        if (res[p[0]] >= res[p[1]]):
            answer += p[0]
        else:
            answer += p[1]
    
    return answer