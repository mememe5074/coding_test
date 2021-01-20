"""
n개의 정수를 이렬ㄹ로 늘어놓은 게임판을 갖고 a와 b가 게임을한다.
게임은 a부터 시작해서 번갈아가며 진행하며, 각 참가자는 자기 차례마다 두 가지 일 중 하나를
할 수 있다. 게임판의 왼쪽 끝에 있는 숫자나 오른쪽 끝에 있는 숫자 중 하나를 가져간다.
가져간 숫자는 판에서 지워진다. 게임판에 두 개 이상의 숫자가 있을 경우, 왼쪽 끝에서 두 개,
혹은 오른쪽 끝에서 두 개를 지운다. 보드판에 숫자가 없으면 게임이 종료되고 각 사람의 점수는
가져간 숫자의 총 합이다. 게임이 끝났을 때 두 사람의 점수 차는 몇인가?
"""
N = int(input())
board = list(map(int, input().split()))

def play(left, right):
    # 모든 수가 없어졌을 때
    if left > right: return 0

    #수를 가져갈 경우
    ret = max(board[left] - play(left + 1, right), board[right] - play(left, right-1))

    #수를 없애는 경우
    if right - left + 1 >= 2:
        ret = max(ret, -play(left + 2, right))
        ret = max(ret, -play(left, right - 2))
    return ret

print(play(0, N-1))
"""
6
100 -1000 -1000 100 -1000 -1000

10
7 -5 8 5 1 -4 -8 6 7 9
"""
