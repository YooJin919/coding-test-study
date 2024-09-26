# 기준 = 영어, 수학의 평균 점수
# 기준으로 학생들의 등수 매기기

def solution(score):
    l = len(score)
    answer = [0] * l
    
    for idx in range(l):
        score[idx] = [score[idx][0]+score[idx][1], idx]
    
    score.sort(reverse=True)
    
    r = 1
    for idx in range(l):
        if(idx != 0 and score[idx][0] == score[idx-1][0]):
            answer[score[idx][1]] = answer[score[idx-1][1]]
        else:
            answer[score[idx][1]] = r
        r += 1
    
    return answer