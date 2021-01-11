"""
양자화 : 더 넓은 범위를 갖는 값들을 작은 범위를 갖는 값들로 근사해 표현하여
자료를 손실 압축하는 과정
1,000 이하의 자연수들로 구성된 수열을 s가지의 자연수만을사용하도록 양자화하려한다.
ex) 1 2 3 4 5 6 7 8 9 10 을 3 3 3 3 3 7 7 7 7 7 로 표현할 수 있다.

이때 우리는 이중 각 숫자별 오차 제곱의 합을 최소화 하는 양자화 결과를 알고 싶다.
ex) 1 2 3 4 5 를 2 2 3 3 3으로 양자화하면 각 숫자별 오차는 -1, 0, 0, 1, 2이고
오차 제곱의 합은 1+0+0+1+4 = 6이다.
"""

N, S = map(int, input().split())
num_list = list(map(int, input().split()))
check = [False]*N
def quantize(cand_list, x):
    #3가지 경우를 모두 골랐을 경우
    if check.count(True) == S:
        Sum = 0
        for i in range(N):
            MIN = 10000000
            for j in range(S):
                MIN = min(pow((num_list[i]-cand_list[j]), 2), MIN)
            Sum += MIN
        return Sum
    else:
        ret = 100000000
        for i in range(N):
            #이미 골랐다면
            if check[i]:
                continue
            #처음 골랐다면
            else:
                check[i] = True
                cand_list.append(num_list[i])
                ret = min(quantize(cand_list, i), ret)
                check[i] = False
                cand_list.remove(num_list[i])
    return ret
emp_list = []
print(quantize(emp_list,0))
#1 744 755 4 897 902 890 6 777