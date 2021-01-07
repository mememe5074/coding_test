"""
보글은 5x5크기의 알파벳 격자를 갖고 하는 게임이다.
이때 게임의 목적은 상하좌우/대각선으로 인접한 칸들의 글자들을
이어서 단어를 찾아내는 것이다. 각 글자들은 대가선으로도 이어질 수 있고,
한 글자가 두 번 이상 사용될 수 있다. 주어진 칸에서 시작해서
특정 단어를 찾을 수 있는지 확인하는 문제를 풀어보자.
"""

"""
1. 위치(y, x)에 요구하는 단어의 첫 글자가 아닌 경우 fail
2. 길이가 1이면 1번 요구를 만족할 시 success

1,2 번을 재귀적으로
"""
# 순서대로 대(좌상) / 좌 / 대(좌하) / 대(우상) / 우 / 대(우하) / 상 / 하
dx = [-1, -1, -1, 1, 1, 1, 0, 0]
dy = [-1, 0, 1, -1, 0, 1, -1, 1]

target = "ABCDE"
MAP = [list(map(str, input().split())) for _ in range(5)]

def find_word(y, x, MAP, target):
    # 배열을 초과했을 경우
    if not(0 <= y <= 4 and 0 <= x <= 4) :
        return False

    # 원하는 글자가 아닐 경우
    if MAP[y][x] != target[0]: return False

    # 찾고자 하는 글자가 나왔을 경우
    if len(target) == 1: 
        return True

    # 인접한 8방향을 탐색한다.
    for i in range(8):
        # Y와 X의 이동
        next_Y = y+dy[i]
        next_X = x+dx[i]

        #재귀적으로 호출하되, 타깃 문자열은 이미 찾은 글자를 슬라이싱하여 사용
        if(find_word(next_Y, next_X, MAP, target[1:] )):
            return True

    return False

find_word(0, 0, MAP, target)