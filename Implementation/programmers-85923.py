def solution(nums):    
    typeCnt = len(set(nums))
    pickCnt = len(nums) // 2
    
    if(typeCnt <= pickCnt):
        return typeCnt
    elif(typeCnt > pickCnt):
        return pickCnt