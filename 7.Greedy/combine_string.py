"""
c언어의 큰 문제점 중 하나는 언어 차원에서 문자열 변수형을 지원하지 않는다는 것이다.
문자 배열로 문자열을 표현하되 NULL을 문자열의 끝으로 지정한다. 문자열의 길이를 쉽게
알 수 있는 방법이 없기 때문에 여러 문제점이 발생한다.
우리는 strcat을 이용하여 n개의 문자열을 순서와 상관없이 합쳐서 한 개의 문자열로 만들고 싶다.
문자열을 합치는 순서는 상관없지만 그 비용은 최소로 하고 싶다.

ex1) al, go, spot
1) al + go = 4
2) algo + spot = 8
총 12 소요

ex1) al, go, spot
1) al + spot = 6
2) alspot + go = 8
총 14 소요
이처럼 n개의 문자열의 길이가 주어질 떄 필요한 최소 비용을 찾는 프로그램을 작성하라.
5
3 1 3 4 1
"""
from collections import deque

N = int(input())
length_str = list(map(int, input().split()))
length_str.sort()
check = [False]*N

def concat(s):
    q = deque()
    for i in range(N):
        q.append(s[i])
    ret = 0

    while len(q) > 1:
        tmp1 = q.popleft()
        tmp2 = q.popleft()
        q.append(tmp1+tmp2)
        # print(q)
        ret += tmp1 + tmp2
    return ret

print(concat(length_str))