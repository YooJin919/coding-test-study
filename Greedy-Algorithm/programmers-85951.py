# 모든 차량이 고속도로에서 단속 카메라를 적어도 한 번 만나도록 설치
# 고속도로 이동 차량의 경로 routes
# 고속도로 진입 지점 routes[i][0], 고속도로 나간 지점 routes[i][1]
# 최소 몇 대의 카메라를 설치해야 하는지 출력

# 나간 지점 기준으로 오름차순 정렬 -> 나간 지점에 카메라 설치 -> 다음 차량이 카메라에 걸리면 pass -> 안걸리면 해당 차량 나간 지점에 카메라 설치

def solution(routes):
    answer = 1
    routes.sort(key = lambda x:x[1])
    lastPos = routes[0][1]
    for car in routes:
        if(car[0] <= lastPos <= car[1]):
            continue
        else:
            lastPos = car[1]
            answer += 1
    
    return answer