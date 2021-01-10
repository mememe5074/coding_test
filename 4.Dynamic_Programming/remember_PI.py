"""
이해못함
"""
sequence = list(map(int, input()))
cache = [-1]*10002
print(sequence)
def classify(a, b):
    M = sequence[a:a+b-1]
    if M.count(M[0]) == len(M):
        return 1

    progressive = True
    #등차수열
    for i in range(len(M)-1):
        if (M[i+1] - M[i]) != (M[0] - M[1]):
            progressive = False
    #등차수열(공차가 1)
    if progressive and abs(M[0]-M[1]) == 1:
        return 2
    
    #두 개의 숫자가 번갈아 나타날 때
    alternating = True
    for i in range(len(M)):
        # 짝수 길이
        if M[i] != M[i%2]:
            alternating=False
    if alternating : return 4
    if progressive : return 5

    return 10

def memorize(begin):
    if begin == len(sequence):
        return 0
    ret = cache[begin]
    if ret != -1:
        return ret
    ret = 1000000
    for i in range(3,6):
        if begin + i <= len(sequence):
            ret = min(ret, memorize(begin+i)+classify(begin, begin+i-1))
    return ret

print(memorize(0))