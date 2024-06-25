def solution(spell, dic):
    answer = 0
    for word in dic:
        for alphabet in spell:
            if(word.count(alphabet) == 1):
                answer = 1
                continue
            else:
                answer = 2
                break
        if(answer == 1):
            return answer
        
    return answer