"""
순서 겹치는 것 고려 x
"""
N = int(input())
s_list = []
for _ in range(N):
    s_list.append(str(input()))

cand_list = list()

check = [False] * len(s_list)
def make_list(now):
    if len(now) == len(s_list):
        temp = list()
        temp.extend(now)
        cand_list.append(temp)
        temp = []
        return
    for i in range(len(s_list)):
        if not check[i]:
            check[i] = True
            now.append(s_list[i])
            make_list(now)
            check[i] = False
            now.pop()


make_list([])
print(cand_list)

def compound(a, b):
    length = min(len(a), len(b))
    if a[:length]==b[-length:]:
        return a[:length]
    
    for i in range(1, length):
        if  a[-length+i:] == b[:length-i]:
            a = a[:-length + i]
            break
    return a+b

for i in range(len(cand_list)):
    for j in range(1, len(cand_list[i])):
        cand_list[i][j] = compound(cand_list[i][j-1], cand_list[i][j])
    print(cand_list[i])

cand_list.sort(key = lambda x: len(x[-1]))
print(cand_list[0][-1])
"""
3
abrac
cadabra
dabr
"""