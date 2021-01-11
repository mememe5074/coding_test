"""
직각 이등변 삼각형형태로 입력이 주어질 때, 맨 위 행에서 맨 아래 행까지
도달해야한다. 이때 지나가는 원소를 더하면서 마지막 행에 도달했을 경우
지나간 원소의 합이 최대가 되도록 경로를 구성하고싶다. 이때 원소의 합과
경로의 개수를 구하시오.
"""

N = int(input())
MAP = []
for _ in range(N):
    MAP.append(list(map(int, input().split())))
way_points = [[-1]*N]*N
CountCache = [[-1]*N]*N
def finding(y, x):
    if y == N-1:
        return MAP[y][x]

    way_points[y][x] = max(finding(y+1, x) , finding(y+1, x+1)) + MAP[y][x]
    return way_points[y][x]
    

def Count(y, x):
    if y == N-1:
        return 1
    
    ret = CountCache[y][x]
    if ret != -1: return ret
    ret = 0
    # 오른쪽 아래 방향이 더 큰 값이라면, 해당 방향으로 카운트
    if(finding(y+1, x+1) >= finding(y+1, x)) : ret += Count(y+1, x+1)
    # 아래 방향이 더 큰 값이라면, 해당 방향으로 카운트
    if(finding(y+1, x+1) <= finding(y+1, x)) : ret += Count(y+1, x)

    return ret

print(Count(0, 0))