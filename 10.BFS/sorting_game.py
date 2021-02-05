"""
정수의 배열이 주어질 때 연속된 부분 구간의 순서를 뒤집는 것을 뒤집기 연산이라고 한다.
예를 들어 {3 4 1 2}에서 부분 구간 {4 1 2}를 뒤집으면 {3 2 1 4}가 된다.
중복이 없는 정수 배열을 뒤집기 연산을 이용하여 뒤집으려고 할 때
필요한 최소한의 뒤집기 수를 계산하라.
4
3 4 1 2
8
3 4 1 2 6 8 7 5
"""
N = int(input())
num_list = list(map(int, input().split()))

from collections import deque


distance = dict()

def bfs(perm):
    queue = deque()
    sorted_list = sorted(perm)
    #처음 주어진 배열에 초기 값을 설정한다.
    distance[str(perm)] = 0
    #처음 주어진 배열을 큐에 넣는다.
    queue.append(perm)

    while queue:
        here = queue.popleft()
        #만약 현재 배열이 정렬되어 있다면
        if here == sorted_list:
            return distance[str(here)]
        #현재 배열의 연산 횟수를 cost에 기록한다
        cost = distance[str(here)]
        #가능한 연산을 모두 구한다.
        for i in range(N):
            #정상적으로 뒤집기 위해 범위를 조정함
            for j in range(i+1, N+1):
                #인덱스에 맞게 뒤집은 다음 here교체
                here = index_reverse(i, j, here)
                #만약 뒤집은 배열이 존재하지 않다면
                if str(here) not in distance:
                    #연산횟수를 늘려준 다음 큐에 넣는다.
                    distance[str(here)] = cost+1
                    queue.append(here)
                #원위치
                here = index_reverse(i, j, here)
    return -1

#주어진 구간을 뒤집는 함수
def index_reverse(i, j, ex_list):
    tmp = ex_list[i:j]
    tmp.reverse()
    tmp.extend(ex_list[j:])
    tmp2 = ex_list[:i]
    tmp2.extend(tmp)
    return tmp2

print(bfs(num_list))