"""
팬 미팅에서 연예인과 팬들이 포옹을한다.
팬미팅에 참가한 M명의 팬들은 줄을 서서 맨 오른쪽 멤버부터
싲가하여 한 명씩 왼쪽으로 움직이면서 멤버들과 포옹을한다.
모든 팬들은 동시에 한명씩 움직인다.
하지만 남성끼리는 포옹대신 악수를 하기로했다.
멤버들과 팬들의 성별이 주어질 때 멤버가 동시에 포옹하는 일은
몇 번이나 있는지 계산하라.

첫 줄에는 멤버들의 성별
둘째 줄에는 팬들의 성별이 주어진다.
"""
"""
크기가 큰 두 정수의 곱으로 해결한다.
"""
member_zender = list(map(str, input().split()))
fan_zender = list(map(str, input().split()))

for i in range(len(member_zender)):
    if member_zender[i]=="F":
        member_zender[i]=0
    else:
        member_zender[i]=1

for i in range(len(fan_zender)):
    if fan_zender[i]=="F":
        fan_zender[i]=0
    else:
        fan_zender[i]=1

def karatsuba(x, y):
    # 각각의 length를 구한다
    strx, stry = str(x), str(y)
    lenx, leny = len(strx), len(stry)

    # Initialize
    if lenx == 1 or leny ==1:
        return x * y

    # Divide
    m = min(lenx, leny) // 2
    a, b = int(strx[:-m]), int(strx[-m:])
    c, d = int(stry[:-m]), int(stry[-m:])

    # Conquer
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a+b, c+d) - ac - bd

    # Combine
    return 10**(2*m) * ac + 10**m * ad_bc + bd

def hug (member_zender, fan_zender):
    N = len(member_zender)
    M = len(fan_zender)
    C = karatsuba(member_zender, fan_zender)
    hug=0
    for i in range(N-1, M):
        hug += 1
    
    return hug
print(hug(member_zender, fan_zender))