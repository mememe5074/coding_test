ex_list = [
    [1, 3, 4, 7],
    [0, 2],
    [1],
    [0, 6],
    [0, 5],
    [4],
    [3, 8],
    [0],
    [6]
]
check = [False for _ in range(len(ex_list))]
distance = [0 for _ in range(len(ex_list))]
parent = [-1 for _ in range(len(ex_list))]
from collections import deque
queue = deque()

def bfs(start):
    queue.append(start)
    check[start] = True
    while queue:
        tmp = queue.popleft()
        print(tmp)
        for i in range(len(ex_list[tmp])):
            there = ex_list[tmp][i]
            #해당 정점을 처음 방문했을 때
            if not check[there]:
                queue.append(there)
                check[there] = True
                #직전에서 간선 1개만 더했을 경우 최단거리
                distance[there] = distance[tmp] + 1
                parent[there] = tmp
bfs(0)
print(distance)
print(parent)