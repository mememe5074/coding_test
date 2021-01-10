"""
nxn 크기의 격자에 1부터 9까지의 정수를 쓴 게임판이 존재한다.
이때 갱엠의 목적은 게임판의 왼쪽 위 칸에서 시작해서 게임판의 맨 오른쪽
아래 칸에 도착하는 것이다. 이때 칸에 적혀있는 숫자만큼 아래 혹은 오른쪽으로 이동할 수 있다.
게임판 밖으로 벗어나는 것은 불가능하다.
게임판이 주어질 때 시작점에서 끝점으로 도달하는 방법이 존재하는지를 판단하라.
"""
#동적 계획법의 첫 단계는 해당 문제를 재귀적으로 해결하는 완전탐색 알고리즘을 만드는 것이다.
MAX = 100
N = int(input())
MAP = []
for _ in range(N):
    MAP.append(list(map(int, input().split())))

# 캐시초기화
cache = [[-1]*MAX]*MAX

# 이동
def move(y, x):    
    #맵을 벗어날 경우
    if not ((0 <= y < N) and (0 <= x < N)): return False
    #기저사례
    if MAP[y][x] == -1 : return True

    jumpSize = MAP[y][x]
    # 아래, 오른쪽 두 경우 중 하나만 성공해도 상관 없으니 다음처럼 표현 가능
    return move(y+jumpSize, x) or move(y, jumpSize + x)

print(move(0,0))

def move_memo(y, x):
    #맵을 벗어날 경우
    if not ((0 <= y < N) and (0 <= x < N)): return False
    #기저사례
    if MAP[y][x] == -1 : return True

    ret = cache[y][x]
    #계산한 적이 있다면 바로 반환
    if ret != -1: return ret

    jumpSize = MAP[y][x]
    ret = move_memo(y+jumpSize, x) or move_memo(y, jumpSize + x)
    return ret
    
print(move_memo(0,0))
"""
2 5 1 6 1 4 1
6 5 1 2 2 9 3
7 2 3 2 1 3 1
1 1 3 1 7 1 2
4 1 2 3 4 1 2
3 3 1 2 3 4 1
1 5 2 9 4 7 -1
"""