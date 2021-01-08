"""
어떤 나라에 n(2~10)개의 큰 도시가 있다.
한 영업우 사원이 한 도시에서 출불하여 다른 모든 도시를 한 번씩
방문한 뒤 시작 도시로 돌아오려고 한다. 각 도시들은 모두 직선으로 연결되었다.
가능한 모든 경로 중 가장 짧은 경로를 구하라
"""
MAX = 1000
INF = 10000000
n = int(input())
# 두 도시간의 거리를 저장하는 배열
dist = [MAX][MAX]
visited = [n]*False

#path : 지금까지의 경로
#visited : 방문처리
#count : 경로의 길이
def shortestPath(path, visited, count):
    #방문을 마쳤으면 돌아가는 경로까지 더해준 뒤 반환한다.
    if len(path)==n: return count + dist[path[0]][path[-1]]
    #가장 큰 값으로 초기화
    ret = INF
    #다음 방문할 도시를 전부 시도한다.
    for Next in range(n):
        #방문했다면
        if visited[Next]: continue
        now = path[-1]
        #방문처리
        visited[Next] = True
        #path에 추가
        path.append(Next)
        cand = shortestPath(path, visited, count+dist[now][Next])
        ret = min(ret, cand)
        visited[Next] = False
        path.pop()
    return ret