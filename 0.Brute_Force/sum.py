#1부터 n까지의 수 합 (반복문)
def sum_for(n):
    ret = 0
    for i in range(n+1):
        ret += i
    return ret

print(sum_for(10))

# 1부터 n까지의 수 합 (재귀함수)
def recursive_sum(n): 
    if n==1:
        return 1
    return n + recursive_sum(n-1)

print(recursive_sum(10))