#메모제이션 동적 프로그래밍 big-O(n^2)

#캐시 초기화
cache = [[-1]*30]*30


def bino_cof(n, r):
    #기저사례
    if n==1 or r==1 : return 1
    
    #만약 이미 계산한 값이라면 그 값을 반환
    if cache[n][r] != -1:
        return cache[n][r]
    #계산한 적이 없다면 재귀호출로 계산
    cache[n][r] = bino_cof(n-1, r-1) + bino_cof(n-1, r)
    return cache[n][r]

print(bino_cof(3,1))