"""
드래곤 커브는 선분 하나에서 시작해서 간단한 규칙으로 이 선분을 변행하여 만들어지며,
변형이 한 번 이루어져 세대가 변할 때마다 더욱 복잡한 모양으로 진화한다.
드래곤 커브 문자열은 F+-XY로 구성된 문자열인데
각각 전진, 왼쪽으로 90도 회전, 오른쪽으로 90도 회전, 무시, 무시를 뜻한다.

0세대 드래곤 컵르ㅡㄹ 그리는 문자열은 선분 하나인 FX이다.
그 이후 다음세대는 이전 세대 문자열의 각 글자를 다음과 같이치환해서 만들어진다.

X -> X + YF
Y -> FX - Y
따라서,
1세대 : FX + YF
2세대 : FX + YF + FX - YF

우리는 n세대 드래곤 커브 문자열을 구하고 싶다. 문자열 전체를 구하면 너무 기니, p부터 l글자만을
계산하는 프로그램을 만들어라.

입력 첫줄에는 커브의 세대 n, 그리고 p와 l이 주어진다.
출력은 n세대 드래곤 커브 문자열의 p번째 글자부터 l까지 글자를 출력한다.
"""

N, P, L = map(int, input().split())
cache = [-1]*N

def dragon_curve(seed, generation, now):
    if generation == 0:
        now.extend(seed)
        return now
    for i in range(len(seed)):
        if seed[i] == 'X':
            #seed가 X라면 세대를 하나 줄이고, X+YF로 연장하여 붙여 넣는다
            dragon_curve("X+YF", generation-1, now)
        elif seed[i] == 'Y':
            #위와 동일
            dragon_curve("FX-Y", generation-1, now)
        else:
            #X나 Y가 아니라면 치환할 것 없이 그대로 붙임
            now.extend(seed[i])
    return now

new_list = dragon_curve('FX', N, [])

for i in range(P-1, P+L-1):
    print(new_list[i], end="")