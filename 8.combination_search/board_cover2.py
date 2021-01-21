"""
포기 미해결. 머리아파서 못하겠음.
HxW크기의 게임판과 한 가지 모양의 블록이 여러개 있다. 게임판에
가능한 많은 블록을 올려놓고 싶은데, 게임판은 검은 칸과 흰칸으로 구성된
격자모양을 하고 있으며 이 중에서 흰칸에만 블록을 올려놓을 수 있다.
게임판과 블록 모양이 주어질 때 최대 몇 개의 블록을 올려놓을 수 있는지
판단하는 프로그램을 작성하라.

첫 줄에는 게임판의 크기 H, W와 블록의 모양을 나타내는 격자의 크기 R, C가
주어진다.
4 7 2 3
1101100
1000000
1000011
1001111
111
100

5 10 3 3
0000000000
0000000000
0000000000
0000000000
0000000000
010
111
001
"""

H, W, R, C = map(int, input().split())
board = []
block = []
block_set = []
best = 0
covered = [[0]*10 for _ in range(10)]
for _ in range(H):
    board.append(list(map(int, input())))

for _ in range(R):
    block.append(list(map(int, input())))

def bolck_rotate(b):
    new = [[] * R for _ in range(C)]

    for i in range(len(b)):
        for j in range(len(b[0])):
            new[j][len(b)-i-1] == b[i][j]
    return new

def generate(b):
    for rot in range(4):
        originY = originX = -1
        for i in range(len(b)):
            for j in range(len(b[i])):
                if b[i][j] == 1:
                    if originY == -1:
                        originX = j
                        originY = i
                    block_set[rot].append( (i-originY ,j-originX) )
        b = bolck_rotate(b)
    block_set.sort()
    blockSize = len(block_set[0])

def check(y, x, b, delta):
    ok = True
    for i in range(len(b)):
        ny = y + b[i][0]
        nx = x + b[i][1]
        if ny < 0 or ny > H or nx < 0 or nx > W:
            ok = False
        board[ny][nx] += delta
        if board[ny][nx] > 1:
            ok = False
    return ok

def fill_board(cnt):
    y = x = -1
    for i in range(H):
        for j in range(W):
            if board[i][j] == 0:
                y=i
                x=j
                break
        if y != -1: break

    if y == -1:
        best = max(best, cnt)
        return
    
    for i in range(len(block_set)):
        if check(y, x, block_set[i], 1):
            fill_board(cnt+1)
        check(y, x, block_set[i], -1)

    covered[y][x] = 1
    fill_board(cnt)
    covered[y][x] = 0

def solve():
    best = 0
    for i in range(H):
        for j in range(W):
            covered[i][j] = board[i][j]
    fill_board(0)
    return best

print(solve())