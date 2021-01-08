"""
HxW 크기의 게임판이 있다. 게임판은 검은 칸과 흰 칸으로 구성된 격자모양이다.
이 중 모든 흰 칸을 세 칸짜리 L자 모양의 블록으로 덮고 싶다.
블록들은 자유롭게 회전해서 놓을 수 있지만, 서로겹치거나, 검은 칸을 덮거나,
게임판 밖으로 나가서는 안된다.
 게임판이 주어질 때 이를 덮는 방법의 수를 계산하라
"""

"""
첫줄에는 두 개의 정수 H(1 이상), W(20이하)가 주어진다.
다음 H줄에 각 W 글자로 게임판의 모양이 주어진다.
#은 검은 칸, .은 흰 칸
"""

#높이와 너비 길이를 입력받음
H, W = map(int, input().split())

MAP = []
#맵을 입력받음
for _ in range(H):
    MAP.append(list(map(int, input())))

#블럭의 모양
L_block = [
    [(0, 0), (0, 1), (1,0)],
    [(0, 0), (0, 1), (1,1)],
    [(0, 0), (1, 0), (1,1)],
    [(0, 0), (1, 0), (1,-1)],
]

#delta에 따라 블록을 채울 수도 치울 수도 있음
def finding(MAP, y, x, Type, delta):
    ok = True
    for i in range(3):
        ny = y + L_block[Type][i][0]
        nx = x + L_block[Type][i][1]

        #맵을 벗어나면
        if not(0 <= ny <= H) or not(0 <= nx <= W):
            ok = False
        #겹치면
        else:
            MAP[ny][nx] += delta
            if(MAP[ny][nx]>1):
                ok = False
    return ok

def filling(MAP):
    # 아직 채우지 못한 칸 중 가장 윗줄 왼쪽에 있는 칸을 찾는다.
    y=x=-1
    for i in range(H):
        for j in range(W):
            if MAP[i][j] == 0:
                y=i
                x=j
                break
        if y != -1: break
    """a모든 칸을 채웠으면 1을 반환, 가장 윗줄에 가장 왼쪽 칸을 찾으므로
    만약 y가 -1이라면 즉, 0인 칸이 존재하지 않는다면 모든 흰 칸을 채운 것"""
    if y==-1 : return 1
    ret = 0
    for i in range(4):
        if(finding(MAP, y, x, i, 1)):
            ret += filling(MAP)
        # 덮었던 블록을 치운다
        finding(MAP, y, x, i, -1)
    return ret

print(filling(MAP))
print(MAP)