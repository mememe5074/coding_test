"""
8 0
6 2 5 1 7 4 8 3
"""

N, K = map(int, input().split())
sequence = list(map(int, input().split()))
cache = [-1]*N
check = [False]*N
new_list = []

def lis(now, start):
    if start == N-1:
        tmp_list = []
        tmp_list.extend(now[1:])
        new_list.append(tmp_list)
        tmp_list = []
        return

    for i in range(start, N):
        start += 1
        if now[-1] < sequence[i] and not check[i]:
            now.append(sequence[i])
            check[i] = True
            lis(now, start)
            now.pop()
            check[i] = False
    return
lis([-1], 0)
new_list.sort(key=len, reverse=True)

print(new_list)
