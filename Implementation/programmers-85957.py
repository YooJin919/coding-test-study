def solution(keyinput, board):
    answer = [0, 0]
    key = {"up": [0, 1], "down": [0, -1], "left": [-1, 0], "right": [1, 0]}
    
    for direct in keyinput:
        if(-(board[0]//2) <= answer[0] + key[direct][0] <= board[0]//2):
            answer[0] += key[direct][0]
        if(-(board[1]//2) <= answer[1] + key[direct][1] <= board[1]//2):
            answer[1] += key[direct][1]
    
    return answer