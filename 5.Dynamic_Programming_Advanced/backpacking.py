"""
        노트북  카메라  엑박    커피그라인더    아령    백과사전
부피    4       2       6       4              2        10
절박도  7       10      6       7              5         4

캐리어의 용량이 정해져 있기 때문에 가져갈 수 있은 물건들의 합은 캐리어의 용량 W이하여야 한다.
이때 절박도를 최대화할 수 있는 물건들의 목록을 계산하는 프로그램을 작성하라.

첫 줄에는 가져가고 싶은 물건의 수와 캐리어의 용량이 주어진다.
다음 줄부터 가져가고 싶은 물건, 부피, 절박도가 주어진다.
6 17
laptop 4 7
camera 2 10
xbox 6 6
grinder 4 7
dumbell 2 5
encyclopedia 10 4
"""
N, W = map(int, input().split())
carrier_list = []
for _ in range(N):
    (a, b, c) = tuple(map(str, input().split()))
    carrier_list.append((a, int(b), int(c)))
check = [False]*N

empty_list = []
def packing(now, hope, weight):
    if weight == W:
        if now not in empty_list:
            empty_list.append(now, hope)
        
        return hope, now
    if weight > W:
        tmp = now[-1]
        hope -= tmp[2]
        weight -= tmp[1]

        if now[:-1] not in empty_list:
            empty_list.append((now[:-1], hope))


        return hope, now
    ret = -1
    for i in range(N):
        #이미 넣은 물건이라면
        if check[i]: continue
        now.append(carrier_list[i])
        weight += carrier_list[i][1]
        hope += carrier_list[i][2]

        check[i] = True
        a, _ = packing(now, hope, weight)
        ret = max(ret, a)
        check[i] = False
        weight -= carrier_list[i][1]
        hope -= carrier_list[i][2]
        now.pop()
    return ret, now

packing([], 0, 0)
empty_list.sort(key=lambda x: x[1])
print( empty_list[-1][1], len (empty_list[-1][0]))
for i in empty_list[-1][0]:
    print(i[0])