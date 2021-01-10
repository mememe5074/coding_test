def fastSum(n):
    # n이 1이면 1을 반환
    if n == 1 : return 1
    # n이 홀수면 분할해서 실행
    if n%2 == 1 : return fastSum(n-1) + n
    return 2*fastSum(int(n/2)) + int((n/2)*(n/2))

print(fastSum(10))