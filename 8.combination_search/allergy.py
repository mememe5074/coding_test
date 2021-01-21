"""
집들이에 n명의 친구를 초대하려고한다. 할 줄 아는 m가지의 음식 중 무엇을
대접해야 할까를 고민하는데, 친구들은 각각 알러지 때문에 못 먹는 음식들이 있어서
아무 음식이나 해서는 안된다. 음식 목록과 해당 음식을 못먹는 친구들의 목록이
다음과 같이 주어질 때, 각 친구가 먹을 수 있는 음식이 최소한 하나씩은 있게 하려면
최소 몇 가지의 음식을 해야 할까요?
첫 줄에는 친구의 수 n과 할 줄 아는 음식의 수 m이 주어진다.
그 후 m줄에 하나씩 각음식에 대한 정보가 주어지는데, 그 정보는 해당 음식을 먹을 수 있는 친구의 수와
각 친구의 이름으로 주어진다.

4 6
cl bom dara minzy
2 dara minzy
2 cl minzy
2 cl dara
1 cl
2 bom dara
2 bom minzy

10 7
a b c d ef g h i j
6 a c d h i j
3 a d i
7 a c f g h i j
3 b d g
5 b c f h i
4 b e g j
5 b c g h i
"""
N, M = map(int, input().split())
name_list = list(map(str, input().split()))
menu_info = []
food_check = [False for _ in range(M)]
people_check = list()

for _ in range(M):
    menu_info.append( list(map(str, input().split())) )

for i in range(M):
    menu_info[i][0] = int(menu_info[i][0])

menu_info.sort(key=lambda x:x[0], reverse=True)

best = 1000000000
def find(cnt, food):
    global best
    if cnt >= best: return
    for i in range(food, len(menu_info)):
        if len(people_check) == N:
            best = cnt
            return
        if food_check[i] != True:
            food_check[i] = True
            tmp=0
            for j in range(1, len(menu_info[i])):
                if menu_info[i][j] not in people_check:
                    tmp += 1
                    people_check.append(menu_info[i][j])
            find(cnt+1, food+1)
            if tmp != 0: 
                for _ in range(tmp) : people_check.pop()
            food_check[i] = False
    return best
    
print(find(0, 1))