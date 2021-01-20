"""
미해결

5x5 크기의 게임판에서 번갈아가며 블럭을 하나씩 게임판에 놓는다.
블록은 L모양의 3칸 짜리블럭과 2칸짜리 블럭이 있으며 항상 게임파네 있는 줄에
맞춰 내려놓아야한다. 블럭은 서로 겹칠 수 없다. 블럭을 더이상 놓을 수 없게 되면
마지막에 올려놓은 사람의 승리다. 게임판이 주어질 때, 해당 차례인 사람이
승리할 수 있는 방법이 무엇이 있는지 판단하라.

"""
board = []
for _ in range(5):
    board.append(list(map(str, input().split())))

shape = [
    [(1,0),(1,0)],
    [(1,1),(0,0)],
    
    [(1,0),(1,1)],
    [(1,1),(0,1)],
    [(1,1),(1,0)],
    [(0,1),(1,1)],
]

def finding(board, y, x, Type, delta):
    ok = True
    for i in range(3):
        ny = y + shape[Type][i][0]
        nx = x + shape[Type][i][1]
    
        #맵을 벗어나면
        if not(0 <= ny <= 4) or not(0 <= nx <= 4):
            ok = False
        else:
            board[ny][nx] += delta
            #겹치면
            if(board[ny][nx]>1):
                ok = False
    return ok

def filling(board):
    x = y = -1
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                y = i
                x = j
                break
        if y != -1: break
    ret = 0
    for i in range(5):
        if finding(board, y, x, i, 1):
            ret += filling(board)
        finding(board, y, x, i, -1)
    return ret
    