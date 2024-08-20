# 왼손 엄지 = *
# 오른손 엄지 = #
# 상하좌우 이동, 한 칸 = 거리 1
# 1, 4, 7 = 왼손
# 3, 6, 9 = 오른쪽
# 2, 5, 8, 0 = 가까운 엄지, 거리 같으면 주 손

def solution(numbers, hand):
    answer = ''
    key = {1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2], 0:[3,1]}
    L, R = [3,0], [3,2]
    
    for n in numbers:
        xx, yy = key[n]
        ll = abs(L[0]-xx) + abs(L[1]-yy)
        rr = abs(R[0]-xx) + abs(R[1]-yy)
        if (n in [1, 4, 7]):
            L = [xx ,yy]
            answer += "L"
        elif (n in [3, 6, 9]):
            R = [xx, yy]
            answer += "R"
        else:
            if (ll > rr or (ll == rr and hand == "right")):
                R = [xx, yy]
                answer += "R"
            elif (ll < rr or (ll == rr and hand == "left")):
                L = [xx ,yy]
                answer += "L"
            
    return answer