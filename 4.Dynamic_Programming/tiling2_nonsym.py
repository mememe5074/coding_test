"""
타일링문제에서 비대칭만 카운트하는 문제
"""
n = int(input())
cache = [-1]*(n+1)
cache2 = [-1]*(n+1)
cache[1] = 1
cache[2] = 2

def filling(x):
    if x <= 1:
        cache[x]=1
        return cache[x]
    if x == 2:
        cache[x]=2
        return cache[x]

    if cache[x] != -1:
        return cache[x]
    else:
        cache[x] = filling(x-1) + filling(x-2)
        return cache[x]

#방법의 수가 너무 클 수 있으므로
MOD = 1000000007
def Count(n):
    #홀수일 때, 한 쪽면만 채우는 방법을 빼주면 대칭인 경우의 수 제거 가능
    if n % 2 == 1:
        ret = (filling(n) - filling(int(n/2)) + MOD) % MOD
        return ret
    #짝수라면, 완전히 n/n이 대칭일 경우와 중앙에 타일두개가 누워있을 경우를 제거하여 대칭 경우의 수 제거
    ret = filling(n)
    ret = (ret - filling(int(n/2)) + MOD) % MOD
    ret = (ret - filling(int(n/2)-1) + MOD) % MOD

    return ret

print(Count(n))
