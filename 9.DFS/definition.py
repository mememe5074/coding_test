from collections import deque

"""
11
1 2
3 4
5 6
7 8
9 10
2
2
3
3
4
4
"""
N = int(input())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

print(graph)
queue = deque()
check = [False]*N

def DFS(start):
    queue.append(start)
    print(start)
    check[start]=True
    while queue:
        x = queue.pop()
        for i in graph[x]:
            if not check[i]:
                DFS(i)
DFS(0)
# BFS(0)