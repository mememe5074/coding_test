"""
4x4의 격자형태로 배치된 열여섯 개의 시계까 있다
시계는 모두 12, 3, 6, 9시를 가리키고 있다.
이 시계를 모두 12시를 가리키도록 바꾸고 싶다
시계를 조작하는 유일한 방법은 열개의 스위치를 조작하는 것으로,
각 스위치들은 모두 적게는 세 걔에서 많게는 다섯 개의 시계에 연결되어 있다
스위치를 누를 때마다 연결된 시계들은 3시간씩 움직인다.
불가능하면 -1일 출력

스위치 : 시계
0 : 0 1 2
1 : 3 7 9 11
2 : 4, 10 14, 15
3 : 0 4 5 6 7
4 : 6 7 8 10 12
5 : 0 2 14 15
6 : 3 14 15
7 : 4 5 7 14 15
8 : 1 2 3 4 5
9 : 3 4 5 9 13

12 6 6 6 6 6 12 12 12 12 12 12 12 12 12 12
12 9 3 12 6 6 9 3 12 9 12 9 12 12 6 6
"""
#각 시계정보를 입력 받음
clock_list = list(map(int, input().split()))
first_clock = clock_list

INF = 1000000000
data_clock = [
    [0, 1, 2],
    [3, 7, 9, 11],
    [4, 10, 14, 15],
    [0, 4, 5, 6, 7],
    [6, 7, 8, 10, 12],
    [0, 2, 14, 15],
    [3, 14, 15],
    [4, 5, 7, 14, 15],
    [1, 2, 3, 4, 5],
    [3, 4, 5, 9, 13]
]

# switch : 스위치 번호
# 
def rotate(clock_list, switch):
    #스위치에 맞게 시계를 회전함
    for j in data_clock[switch]:
        clock_list[ j ] += 3
        #12시 초과 조정
        if clock_list[j] == 15:
            clock_list[j] = 3

def finding(clock_list, switch):
    #12시로 모두 돌아갔을 경우
    if clock_list.count(12) == 16: return 0
    #최대로 돌았을 경우
    if switch == 10 : return INF

    ret = INF
    for i in range(4):
        # 12시로 모두 정렬된 시점 이후로 모든 return은 0이다.
        # 재귀적으로 호출된 finding에서 ret = min(INF , i+0)이므로 i값이 리턴된다.
        # 즉, i값만 더해진 총 합이 최종적으로 리턴하게 된다. 
        ret = min(ret, i + finding(clock_list, switch+1))
        rotate(clock_list, switch)
    return ret

print(finding(clock_list, 0))