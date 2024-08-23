def solution(s):
    n = {"zero":0, "one":1, "two":2, "three":3, "four":4, 
         "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    
    for num in n:
        res = s.find(num)
    
        if(res >= 0):
            print(num, s[res:res+len(num)])
            s = s.replace(s[res:res+len(num)], str(n[num]))
            
    return int(s)