"""
미해결 모르겠음.
아마추어 고고학자인 일리노이 존스는 고대 문명의 흔적을 찾아냈다.
흔적 중에는 고대 언어의 사전도 포함되어 있었는데,
이 사전에 포함된 단어들은 모두 영어의 소문자 알파벳으로 구성되어 있지만 사전에 포함된
단어들의 순서들이 영어와 서로 달랐다. 발굴팀은 단어들이 사전순이 아닌
다른 순서대로 정렬되어 있는지, 아니면 알파벳들의 순서가 영어와 서로 다른 것인지 알고 싶어한다.
존스는 이 언어에서는 알파벳들의 순서가 영어와 서로 다를 뿐, 사전의 단어들은 사전순서대로 배치되었다는
가서을 세웠다. 이 가설이 사실이라고 가정하고 단어의 목록으로부터 알파벳의 순서를 찾아내려한다.
ex gg, kia, lotte, lg, hanhwa가 사전순서대로 적혀있다고 할 때
gg가 kia보다 앞에 오려면 이 언어에서는 g가 k보다 우선이고 같은 원리로 k는 l앞에, l은 h앞에
와야 한다. 따라서 o g k l h의 상대적 순서를 알게된다. 알파벳의 순서를 계산하는 프로그램을 작성하라.
5
gg
kia
lotte
lg
hanhwa

6
dictionary
english
is
ordered
ordinary
this
"""
from collections import deque
N = int(input())
word_list = []

for _ in range(N):
    word_list.append(str(input()))

graph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
adj = [[0]*26 for _ in range(26)]

def makeGroup(words):
    for i in range(N-1):
        for j in range(i+1, N):
            length = min(len(words[j]) , len(words[i]))
            for k in range(length):
               
                if words[j][k] != words[i][k]:
                    a = ord(words[i][k]) - ord('a')
                    b = ord(words[j][k]) - ord('a')
                    adj[a][b] = 1
                    break
                

makeGroup(word_list)
seen = [False] * len(adj)
order = list()
def dfs(here):
    seen[here] = True
    for there in range(len(adj)):
        #방문한 적이 없고, 위상이 있다면
        if adj[here][there] and not seen[there]:
            dfs(there)
    order.append(here)

def topologicalSort():
    order.clear()
    for i in range(len(adj)):
        if not seen[i]:
            dfs(i)
    order.reverse()
    for i in range(len(adj)):
        for j in range(i+1 ,len(adj)):
            if adj[ order[j] ][ order[i] ]:
                return []
    return order

print(topologicalSort())