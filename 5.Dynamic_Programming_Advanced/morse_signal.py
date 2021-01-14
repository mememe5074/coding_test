"""
n개의 장점과 m개의 단점이 주어지고,
사전순서대로 배열하였을 경우 k번째 모스부호는 무엇인지
출력하는 프로그램을 만들어라

각각의 아스키,
1은 45
0은 111 이기 때문에

"""
N, M, K = map(int, input().split())
sample = []
for _ in range(N):
    sample.append(1)
for _ in range(M):
    sample.append(0)
length = N+M

empty_list = []

def make(now, n, m):
    if len(now) == length:
        if now not in empty_list:
            tmp_list = []
            tmp_list.extend(now)
            empty_list.append(tmp_list)
            tmp_list.clear
        return now
    
    for i in range(length):
        if sample[i]==1 and n > 0:
            n -= 1
            now.append(sample[i])
            make(now, n, m)
            now.pop()
            n += 1
        elif sample[i]==0 and m > 0:
            m -= 1
            now.append(sample[i])
            make(now, n, m)
            now.pop()
            m += 1
    return
make([], N, M)

def calculate(m):
    store = [0]*len(m)
    for i in range(len(m)):
        if m[i] == 1:
            store[i] = (2**i) * 45
        else :
            store[i] = (2**i) * 112
    return sum(store)
new_list = []
for i in range(len(empty_list)):
    # print(calculate(empty_list[i]))
    new_list.append((empty_list[i] ,calculate(empty_list[i]) ))

new_list.sort(key = lambda x: x[1])
print(new_list[K-1][0])
