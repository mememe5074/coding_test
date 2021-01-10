"""
직각이등변삼각형으로 배치된 자연수들이 존재한다.
직각이등변삼각형은 아래로 갈수록 그 너비가 커지는 모양이다.
맨 위의 숫자에서 시작해서 한 번에 아래로 내려가 맨 아래 줄까지 닿는 경로를
만들고자한다. 이때 모든 경로 중 숫자의 합을 최대화하는 경로는 무엇일까?
경로는 바로 아래 또는 바로 아래의 오른쪽위치로 이동할 수 있다.
"""

"""
총 N번 만큼 움직일 수 있다.
해당 칸까지 왔을 때의 최댓값을 갈아치워 넣음
"""
N = int(input())
MAP = []
for _ in range(N):
    MAP.append(list(map(int, input().split())))

cache = [[-1]*N]*N

def move(y, x):
    #기저사례
    if y == N-1: 
        return MAP[y][x]
    # 두 경로중 큰 값만 취하여 이동한다.
    ret = max(move(y+1, x), move(y+1, x+1)) + MAP[y][x]
    return ret

print(move(0, 0))