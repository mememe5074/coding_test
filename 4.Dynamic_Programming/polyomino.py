"""
정사각형들의 변들을 서로 완전하게 붙여 만든 도형들을 폴리오미노라고 부른다.
n개의 정사각형으로 구성된 폴리오미노들을 만들려고 하는데,
이 중 세로로 단조인 폴리오미노의 수가 몇 개나 되는지 알고싶다.
세로로 단조라는 말은 어떤 가로줄도 폴리오미노를 두 번 이상 교차하지 않는다는 뜻이다.

n개의 정사각형으로 구성된 세로 단조 폴리오미노의 개수를 세는 프로그램을 작성하라.
"""
N = int(input())
p_list = []
ret = []
cnt = 0
def make_set(N, now, Org):
    global ret
    if sum(now)==Org:
        cnt = 0
        # 길이가 1일 경우
        if len(now) == 1 or len(now)==Org:
            cnt = 1
            return cnt
        else :
            for i in range(1, len(now)):
                if now[i-1]==1 and now[i]==1: continue
                cnt += now[i-1] + now[i] -1

        return cnt

    for i in range(1, N+1):
        now.append(i)
        first = i
        tmp = (make_set(N-first, now, Org))
        if type(tmp)==int: ret.append(tmp)
        now.pop()
    return ret

new_list = make_set(N, [], N)
print(sum(new_list))

# MOD = 100000000000
# cache = [[-1]*101]*101
# N = int(input())
# def poly(n ,first):
#     if n==first: return 1

#     ret = cache[n][first]

#     if not(ret==-1):
#         return ret
#     ret = 0
#     for s in range(1, n-first+1):
#         add = s + first - 1
#         add *= poly(n-first, s)
#         add= (add + MOD) % MOD
#         ret += add
#         ret = (ret + MOD) % MOD
#     return ret

# print(poly(N, 0))