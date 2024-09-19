# 문자열의 알파벳을 index만큼 뒤의 알파벳으로 변경
# 변경하는 중의 알파벳이 skip에 해당하면 점프

def solution(string, skip, index):
    answer = ''
    skip = list(skip)
    
    for s in string:
        i = index
        
        while i:
            s = chr(ord(s) + 1)
            
            if ord(s) == 123:
                s = 'a'
                
            if s in skip:
                continue
                
            i -= 1
        answer += s
        
    return answer