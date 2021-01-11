"""
2xn 크기의 사각형을 2x1, 1x2 크기의 타일로 채우는 방법의 수를 계산하라.
"""
n = int(input())
check = [-1]*(n+1)
check[1] = 1
check[2] = 2

def filling(x):
    if x <= 1:
        check[x]=1
        return check[x]
    if x == 2:
        check[x]=2
        return check[x]

    if check[x] != -1:
        return check[x]
    else:
        check[x] = filling(x-1) + filling(x-2)
        return check[x]

print(filling(n))