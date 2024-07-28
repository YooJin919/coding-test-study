# 꼭대기 -> 바닥 경로 중 숫자의 합이 가장 큰 경우 출력

def solution(triangle):
    answer = 0
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if (j-1 < 0):
                triangle[i][j] += triangle[i-1][j]
            elif (j == len(triangle[i])-1):
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])            
    return max(triangle[len(triangle)-1])