"""
너비가 같은 N개의 판자를 붙여 세운 울타리가 존재한다.
울타리의 판자들이 부러지거나 망가져 높이가 달라져 울타리를 통째로
교체할 것이다. 하지만 괜찮은 부분은 남겨두고 싶은데, 이때 가장 넓이가
넓은 직사각형의 형태로 보관하고 싶다.
(판자의 너비는 1로 통일)

첫 줄에는 판자의 수 N(1~20,000)가 주어진다.
다음 줄에는 각 판자의 높이가 주어진다.(높이는 10,000이하)
"""

"""
넓이는 어차피 너비가 1이기 때문에 높이만 더해도 된다.

"""

N = int(input())
height_list = list(map(int, input().split()))

def solve(left, right):
    # 기저 사례: 판자가 하나일 경우
    if left == right: return height_list[left]
    mid = int((left+right)/2)
    # 분할하여 각개격파한다.
    ret = max(solve(left, mid), solve(mid+1, right))
    
    # 두 부분에 걸치는 사각형 중 가장 큰 것을 찾는다.
    lo = mid
    hi = mid+1
    height = min(height_list[lo], height_list[hi])
    ret = max(ret, height*2)
    # 사각형이 입력 전체를 덮을 때까지 확장한다.
    while (hi < right) or (left < lo):
        # 항상 더 높이가 높은 쪽으로 확장한다.
        # hi가 오른쪽 끝에 도달하지 못하였고, lo가 왼쪽끝에 닿거나 lo-1번째 높이보다 hi+1의 높이가 크다면
        if (hi < right) and ((lo==left) or height_list[lo-1] < height_list[hi+1]):
            hi += 1
            height = min(height, height_list[hi])
        else:
            lo -= 1
            height = min(height, height_list[lo])
        ret = max(ret, height*(hi-lo+1))
    return ret
print(solve(0, N-1))