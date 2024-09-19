# 치킨 한 마리당 쿠폰 한 장
# 쿠폰 10장 = 1마리 서비스
# 서비스 치킨도 쿠폰 한 장
# 최대 서비스 치킨 수 출력

def solution(chicken):
    answer = 0
    coupon = chicken
    
    while(coupon >= 10):
        answer += coupon // 10
        coupon = (coupon // 10) + (coupon % 10)
    
    return answer