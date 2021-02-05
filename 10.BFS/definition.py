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

from collections import deque
queue = deque()

def bfs(start):
    queue.append(start)
    check[start] = True
    while queue:
        tmp = queue.popleft()
        print(tmp)
        for i in range(len(ex_list[tmp])):
            if not check[ex_list[tmp][i]]:
                queue.append(ex_list[tmp][i])
                check[ex_list[tmp][i]] = True
bfs(0)