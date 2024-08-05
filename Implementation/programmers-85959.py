# 직사각형 공원 -> 이동 가능 O, 이동 불가 X
# 입력된 명령에 따라 산책 진행
# [방향 거리, 방향 거리] -> E 5 (동쪽으로 5칸 이동)

# 명령에 따라 이동했을 때 공원 안인지 확인 / "이동 경로"에 장애물 존재하는지 확인 -> 하나라도 해당시 다음 명령 수행
# 마지막 위치 출력 [세로 방향 좌표, 가로 방향 좌표]

def solution(park, routes):
    cur = []
    r = len(park)
    c = len(park[0])
    d = {"N":[-1, 0], "S":[1, 0], "W":[0, -1], "E":[0, 1]}
    
    # 시작 지점 찾기
    for i in range(r):
        for j in range(c):
            if(park[i][j] == "S"):
                cur = [i, j]

    # 명령 수행
    for cmd in routes:
        canMove = False
        op, n = cmd.split()
        rr = cur[0] + (d[op][0] * int(n))
        cc = cur[1] + (d[op][1] * int(n))

        if(0 <= rr < r and 0 <= cc < c):
            for i in range(1, int(n)+1):
                dd = d[op]
                if (park[cur[0] + (dd[0] * i)][cur[1] + (dd[1] * i)] == "X"):
                    canMove = False
                    break
                canMove = True
        if(canMove):
            cur = [rr, cc]
    
    return cur