"""
마지막 계란 가격이 올랐을 때, 종욱이는 광고판에 꽂힌 플라스틱 판의 순서만 바꿨다.
마지막 계란 가격은 사탕의 가격의 m 배수였다.
지금 계란 가격 e와 m이 주어질 때,
가능한 이전의 계란 가격이 몇가지가 있는지 계산하는 프로그램을 작성하라.
"""

e, m = map(int, input().split())
s = str(e)
num_list = []
for i in range(len(s)):
    num_list.append(s[i])
# print(num_list)

#현재 금액보다 같거나 크면 안된다.
#재배치한 금액은 m의 배수이다.

check = [False] * len(s)
new_list = []
def change(now, cnt):
    if len(now)==len(s) and sum(now) < e :
        if now not in new_list and sum(now)%m==0:
            tmp_list = []
            tmp_list.extend(now)
            new_list.append(tmp_list)
            tmp_list = []
        return now

    for i in range(len(num_list)):
        cnt += 1
        if not check[i]:
            check[i] = True
            tmp = int(pow(10, len(s) - len(now)-1)) * int(num_list[i])
            now.append(tmp)
            change(now, cnt)
            now.pop()
            check[i] = False

change([], -1)
print(len(new_list))