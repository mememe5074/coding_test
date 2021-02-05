"""
감시 카메라 설치
미술관은 여러 개의 갤러리오 이들을 연결하는 복도로 구성되어 있다.
한 갤러리에 감시 카메라를 설치하면 해당 갤러리와 함께 해당 갤러리 복도로 직접
연결된 갤러리들을 모두 감시할 수 있다. 모든 갤러리를 감시하기 위해서 최소 감시카메라의
개수는 몇 개일까?
입력 첫 줄에는 미술관에 포함된 갤러리 수와 갤러리를 연결하는 복도의 수가 주어진다.
각 갤러리에는 0번부터 g-1까지의 고유번호가 있다. 
그 후 h줄에 각 두개의 정수로 복도가 연결하는 두 갤러리의 번호가 주어진다.
6 5
0 1
1 2
1 3
2 5
0 4
"""
g, h = map(int, input().split())
graph = [[] for _ in range(g)]
for _ in range(h):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

check = [False for _ in range(g)]

installed = 0

def dfs(now):
    check[now] = True
    global installed
    children = [0 ,0, 0]
    for i in range(len(graph[now])):
        there = graph[now][i]
        if not check[there]:
            children[dfs(there)] += 1
    #자손 노드 중 감시되지 않는 노드가 있을 경우 카메라를 설치한다.
    if children[0]:
        installed += 1
        return 2
    #자손 노드 중 카메라가 설치된 노드가 있을 경우 설치할 필요가 없다.
    if children[2]:
        return 1
    return 0

for i in range(g):
    #방문안한 갤러리 중 
    if (not check[i]) and dfs(i) == False:
        installed += 1

print(installed)