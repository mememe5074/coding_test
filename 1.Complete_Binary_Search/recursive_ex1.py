"""
0부터 차례대로 번호가 매겨진 n개의 원소 중 네 개를 고르는 모든 경우를 출력하라
ex) n=7이면 (0,1,2,3), (0,1,2,4), (0,1,2,5) ~ (3,4,5,6)의 모든 경우를 출력
단, 재귀호출로 해결하라.
"""

"""
순열이 아니라 조합이므로 (0,1,2,3) = (1,2,3,0)이나 같은 것으로 취급한다.
따라서, 다음 규칙을 따르면 된다.
1) 뽑힌 숫자보다 더 큰 숫자를 골라야함.
2) 뽑힌 숫자는 또 뽑을 수 없다.
3) 4개의 원소를 만족하면 종료(포함o)
4) 뽑은 원소의 개수가 4보다 작고 뽑은 원소보다 큰 숫자가 없으면 종료(포함x)
"""
n = int(input()) #n 입력

empty_list = []

# count : 총 경우의 수
count = 0

#num : 전체 원소의 수, picked_list : 뽑힌 원소들, to_pick : 남은 원소들의 수
def pick_num(num, picked_list, to_pick):
    # 총 4개의 원소를 다 채웠을 경우
    if to_pick==0:
        global count
        count += 1
        return print(picked_list)
    
    if picked_list:
        # 고를 수 있는 가장 작은 원소를 택함
        Min = picked_list[-1] + 1
    else:
        # 더 뽑을 원소가 없다면 0이 최소
        Min = 0
    # 뽑은 숫자로 부터 num까지 for문을 순회
    for i in range(Min, num):
        # Min부터 차례대로 리스트에 넣음
        picked_list.append(i)
        # 재귀적으로 다음 차례 진행하면서 뽑아야할 횟수 차감
        pick_num(num, picked_list, to_pick-1)
        # 다음 순회에 영향을 끼치지 않기 위해 리스트내 넣어줬던 원소를 꺼냄
        picked_list.pop()

pick_num(n, empty_list, 4)
print(count)