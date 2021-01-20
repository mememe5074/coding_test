"""
경기 순서대로 각 팀 선수의 rating이 주어질 때
한국 선수들이 최대한 승리를 가져갈 때 몇 승을 하는가?
6   
3000 2700 2800 2200 2500 1900
2800 2750 2995 1800 2600 2000
"""
N = int(input())
rus = list(map(int, input().split()))
kor = list(map(int, input().split()))

count = 0
rus.sort(reverse=True)
kor.sort(reverse=True)

def order(RUS, KOR):
    wins = 0
    for i in range(N):
        #한국선수 중 가장 점수가 높은 선수가 이길 수 없는 경우
        #한국선수 중 가장 점수가 낮은 선수와 매치시킴
        if KOR[0] < RUS[i]:
            KOR.pop()
        else:
            for j in range(len(KOR)):
                if j < RUS[i]:
                    break
            KOR.remove(KOR[j-1])
            wins += 1
    return wins

print(order(rus, kor))