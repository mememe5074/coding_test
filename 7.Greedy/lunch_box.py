"""
도시락 n개를 주문했지만 전자레인지는 하나밖에 없는 상황이다.
전자레인지가 작아 한 번에 하나의 도시락밖에 데울 수 없다.
i번째 도시락을 데우는 데는 mi초가 걸리고 먹는데는 ei초가 걸린다.
도시락은 나누어 데울 수 없다. 이런 상황에서 우리는 점심을 먹는 데 걸리는 시간을
최소화 하고싶다. 어느 순서로 도시락을 데워야 가장 빨리 점심시간을 마칠 수 있을지
결정하는 프로그램을 작성하라.

첫 줄에는 도시락의 수
두 번째 줄에는 각 도시락을 데우는 데 걸리는 시간
세 번째 줄에는 각 도시락을 먹는 데 걸리는 시간
"""
N = int(input())
lunch_list = []

temp_list1 = list(map(int, input().split()))
temp_list2 = list(map(int, input().split()))

for i in range(N):
    lunch_list.append((temp_list1[i], temp_list2[i]))
    
#먹는데 오래걸리는 것부터
lunch_list.sort(key = lambda x:x[1], reverse=True)

print(lunch_list)

time = lunch_list[N-1][1]

for i in range(N):
    time += lunch_list[i][0]

print(time)