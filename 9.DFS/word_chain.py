"""
끝말잇기
단어 들의 목록이 주어질 때, 단어들을 전부 사용하고 게임이 끝날 수 있는지,
그럴 수 있다면 어떤 순서로 단어를 사용해야 하는지를 계산하는 프로그램을 작성하라.

4
need
god
dog
dragon

5
need
dragon
ton
numerilc
cat
"""
from collections import deque

N = int(input())
word_list = []
for _ in range(N):
    word_list.append(str(input()))

adj = [[0 for _ in range(26)] for _ in range(26)]
graph = [ [0 for _ in range(2)]  for _ in range(26)]
oddCount = []
queue = deque()

def makeGraph(words):
    for i in words:
        start = ord(i[0]) - ord('a')
        end = ord(i[-1]) - ord('a')
        graph[start][0] += 1
        graph[end][1] += 1
        adj[start][end] += 1

def decide(g):
    for i in range(len(g)):
        tmp = sum(g[i])
        if tmp == 0: continue
        elif tmp%2!=0:
            oddCount.append(i)
    #홀수점이 2개 이상이면 불가능
    if len(oddCount) > 2:
        return 0
    #홀수점이 2개일 때 시작점, 끝점 설정
    elif len(oddCount) == 2:
        return 1
    #홀수점이 없을 때
    else:
        return 2

def findRandomCircuit(here, circuit):
    for there in range(len(adj)):
        while adj[here][there] > 0:
            adj[here][there] -= 1
            findRandomCircuit(there, circuit)
    circuit.append(here)
    return circuit

def final():
    if Type == 0:
        print("IMPOSSIBLE")
        return
    elif Type == 1:
        adj[oddCount[0]][oddCount[1]] += 1
        tmp_list = findRandomCircuit(oddCount[0], [])
    else:
        for i in range(len(graph)):
            if sum(graph[i])>0:
                tmp_list = findRandomCircuit(i, [])
                break
    #넣은 순서를 뒤집어서 정방향으로 바꿈
    tmp_list.reverse()
    
    check = [False for _ in range(N)]
    for i in range(1, len(tmp_list)):
        for j in range(len(word_list)):
            #양쪽 글자가 맞는 단어를 가져오기 위함
            s =ord(word_list[j][0])-ord('a')
            e = ord(word_list[j][-1])-ord('a')
            #단어가 겹칠 수 있으므로 방문기록을 통해 중복 피함
            if s == tmp_list[i-1] and e == tmp_list[i] and not check[j]:
                check[j] = True
                print(word_list[j], end=" ")

makeGraph(word_list)
Type = decide(graph)
final()