"""
소풍을 갈 때 학생들이 두 명씩 짝 지어 행동하게 하려한다.
친구끼리 짝을 지어주어야 한다. 각 학생들의 쌍에 대해 이들이
서로 친구인지에 대한 여부가 주어질 때, 학생들을 짝 지을 수 있는
방법의 수를 계산하라.

ab / cd / ef
ab / cf / ed
는 서로 다른 방법이다.

테스트 케이스의 첫 줄은 학생의 수 n( 2 ~ 10 )와
친구 쌍의 수 m ( 0 ~ n(n-1)/2 )가 주어진다.

그 다음 줄에 m개의 정수 쌍으로 서로 친구인 두 학생의 번호가 주어진다.
학생들의 수는 항상 짝수이다.
"""
n = int(input()) # 학생의 수
m = int(input()) # 입력되는 친구 쌍의 수
friend_list = [ list([0]*2)] * int(m)


friend_list_A = list(map(int, input().split()))

j=0
for i in range(int(m)):
    friend_list[i] = [friend_list_A[j], friend_list_A[j+1]]
    j += 2

checking = [False]*n
tmp = []
set(tmp)
count = 0

def make_friends(friend_list, num, made):
    global count
    global tmp
    
    #짝짓기에 성공할 경우
    if len(made)==int(num/2):
        made.sort(key=lambda x:x[0])
        if made not in tmp:
            tmp.extend(made)
            
            count += 1
    
    for i in friend_list:
        if (not checking[i[0]]) and (not checking[i[1]]):
            #짝지어서 넣어줌, 순서를 특정하여 중복 방지
            made.append([min(i[0],i[1]), max(i[0],i[1])])
            #방문처리
            checking[i[0]] = checking[i[1]] = True
            #재귀적으로 다시 돌림
            make_friends(friend_list[1:], num, made)
            #끝나면 원위치
            checking[i[0]] = checking[i[1]] = False
            made.pop()
        else:
            continue


make_friends(friend_list, n, [])

#출력 재정렬
new_list = []
k=0
for _ in range(int(len(tmp)/3)):
    new_list.append( [tmp[0+k], tmp[1+k], tmp[2+k]] )
    k += 3

#중복제거
a_list = []
for v in new_list:
    if v not in a_list:
        a_list.append(v)
print(len(a_list))