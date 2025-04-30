# Q. 재현이는 주변을 살펴보던 중 체스판과 말을 이용해서 새로운 게임을 만들기로 했다.
# 새로운 게임은 크기가 N×N인 체스판에서 진행되고, 사용하는 말의 개수는 K개이다.
# 말은 원판모양이고, 하나의 말 위에 다른 말을 올릴 수 있다.
# 체스판의 각 칸은 흰색, 빨간색, 파란색 중 하나로 색칠되어있다.
#
# 게임은 체스판 위에 말 K개를 놓고 시작한다. 말은 1번부터 K번까지 번호가 매겨져 있고, 이동 방향도 미리 정해져 있다. 이동 방향은 위, 아래, 왼쪽, 오른쪽 4가지 중 하나이다.
#
# 턴 한 번은 1번 말부터 K번 말까지 순서대로 이동시키는 것이다. 한 말이 이동할 때 위에 올려져 있는 말도 함께 이동한다. 말의 이동 방향에 있는 칸에 따라서 말의 이동이 다르며 아래와 같다. 턴이 진행되던 중에 말이 4개 이상 쌓이는 순간 게임이 종료된다.
#
# 1. 1번 말이 이동하려는 칸이
#     1) 흰색인 경우에는 그 칸으로 이동한다. 이동하려는 칸에 말이 이미 있는 경우에는 가장 위에 1번 말을 올려놓는다.
#          - 1번 말의 위에 다른 말이 있는 경우에는 1번 말과 위에 있는 모든 말이 이동한다.
#          - 예를 들어, 1, 2, 3로 쌓여있고, 이동하려는 칸에 4, 5가 있는 경우에는 1번 말이 이동한 후에는 4, 5, 1, 2, 3가 된다.
#      2) 빨간색인 경우에는 이동한 후에 1번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 바꾼다.
#          - 1, 2, 3 가 이동하고, 이동하려는 칸에 말이 없는 경우에는 3, 2, 1가 된다.
#          - 1, 4, 6, 7가 이동하고, 이동하려는 칸에 말이 5, 3, 2로 있는 경우에는 5, 3, 2, 7, 6, 4, 1가 된다.
#       3) 파란색인 경우에는 1번 말의 이동 방향을 반대로 하고 한 칸 이동한다. 방향을 반대로 바꾼 후에 이동하려는 칸이 파란색인 경우에는 이동하지 않고 가만히 있는다.
#       4) 체스판을 벗어나는 경우에는 파란색과 같은 경우이다.
#
# 다음은 크기가 4×4인 체스판 위에 말이 4개 있는 경우이다.
# [그림]
#
# 체스판의 크기와 말의 위치, 이동 방향이 모두 주어졌을 때,
# 게임이 종료되는 턴의 번호를 반환하시오.
#
# 그 값이 1,000보다 크거나 절대로 게임이 종료되지 않는 경우에는 -1을 반환한다.
#
# 입력
# 각 정수는 칸의 색을 의미한다. 0은 흰색, 1은 빨간색, 2는 파란색이다.
# 말의 개수와 체스판의 정보, 현재 말의 위치와 방향을 주어진다.
# 말의 정보는 세 개의 정수로 이루어져 있고,
# 순서대로 행, 열의 인덱스, 이동 방향이다.
# 행과 열의 번호는 0부터 시작하고, 이동 방향은 0, 1, 2, 3 이고
# 0부터 순서대로 →, ←, ↑, ↓의 의미를 갖는다.
#
# k = 4  # 말의 개수
#
# chess_map = [
#     [0, 0, 2, 0],
#     [0, 0, 1, 0],
#     [0, 0, 1, 2],
#     [0, 2, 0, 0]
# ]
# start_horse_location_and_directions = [
#     [1, 0, 0],
#     [2, 1, 2],
#     [1, 1, 0],
#     [3, 0, 1]
# ]
# # 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!

# <문제분석>
# 크기가 N x N 인 체스판
# 사용하는 말의 개수는 K개
# 체스판의 각 칸은 흰색, 빨간색, 파란색 중 하나로 색칠되어 있다 -> 3 가지 케이스
# 하나의 말 위에 다른 말을 올릴 수 있다

# 체스판 위에 말 K개를 놓고 시작한다
# 말은 1번부터 K번까지 번호가 있고, 이동 방향도 미리 정해져 있다
# 이동 방향은 위, 아래, 왼쪽, 오른쪽 4가지 이다 -> 이동 방향도 4가지
# 턴 한 번은 1번부터 K번까지 순서대로 이동시키는 것을 의미한다
# 한 말이 이동할 때는 위에 올려져 있는 말도 함께 이동한다

# [종료조건]
# 턴이 진행되던 중 말이 4개 이상 쌓이는 순간 종료

# [동작]
# 1번 말이 이동하려는 칸이
# 흰색) 그 칸으로 이동하고 그 칸에 말이 이미 있으면 가장 위에 1번 말을 올린다
# 1번말 위에 다른 말이 있는 경우에는 위에 있는 모든 말도 같이 움직인다
# 빨간색) 이동한 후에 1번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 바꾼다
# 파란색) 1번 말의 이동 방향을 반대로 하고, 한 칸 이동한다
# 만약 그 이동하려는 칸이 또 파란색이면 이동하지 않고 가만히 있는다
# 체스판을 벗어나는 경우) 파란색과 같다

# [given & result]
# 체스판의 크기와 말의 위치, 이동 방향이 모두 주어졌을 때
# *게임이 종료되는 턴의 번호를 반환
# 각 정수는 칸의 색을 의미 : 0) 흰색, 1) 빨간색, 2) 파란색
# 말의 개수, 체스판의 정보, 현재 말의 위치와 방향이 주어짐
# 말의 정보는 세 개의 정수
# 행과 열의 번호는 0부터 시작, 이동 방향은 0, 1, 2, 3 (동, 서, 북, 남)

# <문제풀이>
# *턴마다 1번부터 K번까지 이동하면서 4개가 쌓이면 종료
# => 2중 for문?
# 각 말에 말이 쌓이는 것을 저장해놔야 한다
# 1번말에 2번이 쌓여 있고 이것이 다시 3번 말 위에 쌓일 수도 있고
# 쌓이는 순서가 바뀔수도 있다
# *맵에서 어떻게 체스 말들이 쌓여 있는지 저장해야 되고
# => 체스판과 비슷하게 2차원 배열의 원소 각각에 리스트(stack)를 저장해둬야 한다
# *쌓인 순서대로 같이 이동해야 하다 -> stack 을 써야한다
# =>

k = 4  # 말의 개수

chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
start_horse_location_and_directions = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!




# 동 서 북 남
# →, ←, ↑, ↓
dr = [0, 0, -1, 1] # 상, 하
dc = [1, -1, 0, 0] # 좌, 우

# 현재 말이 어떻게 쌓여있는지
# current_stacked_horse_map = [
#     [[0], [1], [2], 0],
#     [0, 0, 0, 0],
#     [0, 0, [3], 0],
#     [0, 0, 0, 0]
# ]

# 반대로 가려면? 방향은 '0, 1, 2, 3' = '동 서 북 남' 이므로
# 0 -> 1
# 1 -> 0
# 2 -> 3
# 3 -> 2
# 수식화 할 수 있으면 좋은데 그냥 직관적으로 if문 걸어서 각 케이스 return 해도 괜찮다
def get_d_index_when_go_back(d):
    if d % 2 == 0:
        return d + 1
    else:
        return d - 1

def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    n = len(game_map) # 정사각형이므로 n 만 구해놓기
    turn_count = 1
    # 현재 말이 어떻게 쌓여 있는지 저장; 행 배열에 들어가는 요소 x 열
    current_stacked_horse_map = [ [ [] for _ in range(n)] for _ in range(n)]
    # print("current_stacked_horse_map : ", current_stacked_horse_map)
    # 각 말들이 어느 위치에 존재하는지 초기화
    for i in range(horse_count):
        r, c, d = horse_location_and_directions[i]
        current_stacked_horse_map[r][c].append(i) # current_stacked_horse_map[0][0] = [0]
    # print("current_stacked_horse_map : ", current_stacked_horse_map)

    while turn_count <= 1000: # 최대 가능 턴
        for horse_index in range(horse_count): # 말의 개수
            r, c, d = horse_location_and_directions[horse_index]
            new_r = r + dr[d] # 다음에 이동 하려는 위치; 물론 이대로 이동하지는 않지만
            new_c = c + dc[d]
            # 3. 파란색
            # 1번 말의 이동 방향을 반대로 하고, 한 칸 이동한다
            # 체스판을 벗어나는 경우) 파란색과 같다
            if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                new_d = get_d_index_when_go_back(d)
                new_r, new_c = r + dr[new_d], c + dc[new_d]
                # 말의 방향이 바뀌므로 방향도 저장해줘야 한다
                horse_location_and_directions[horse_index][2] = new_d
                # 만약 그 이동하려는 칸이 또 파란색이면 이동하지 않고 가만히 있는다
                if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                    continue

            # 1. 흰색
            # 그 칸으로 이동하고 그 칸에 말이 이미 있으면 가장 위에 1번 말을 올린다
            # 1번말 위에 다른 말이 있는 경우에는 위에 있는 모든 말도 같이 움직인다
            moving_horse_index_array = [] # 이동하려는 말들
            for i in range(len(current_stacked_horse_map[r][c])): # 현재 칸에 어떻게 쌓여 있었는지 본다
                current_stacked_horse_index = current_stacked_horse_map[r][c][i]

                if horse_index == current_stacked_horse_index: # 지금 이동하려는 말이면
                    moving_horse_index_array = current_stacked_horse_map[r][c][i:] # 그 말과 그 위로 있는 말을 이동할 수 있다
                    current_stacked_horse_map[r][c] = current_stacked_horse_map[r][c][:i] # 남아있는 말은 그대로 둔다
                    break
            # 2. 빨간색
            # 이동한 후에 1번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 바꾼다
            if game_map[new_r][new_c] == 1:
                moving_horse_index_array = reversed(moving_horse_index_array)

            # 위 까지 이동하려는 말 array를 구했으므로 아래 부터는 실제 이동 구현
            for moving_horse_index in moving_horse_index_array:
                current_stacked_horse_map[new_r][new_c].append(moving_horse_index)
                horse_location_and_directions[moving_horse_index][0], horse_location_and_directions[moving_horse_index][1] = new_r, new_c # 각 말의 현재 위치 업데이트 해줘야한다! 놓치면 안된다

            # 턴이 진행되던 중 말이 4개 이상 쌓이는 순간 종료
            if len(current_stacked_horse_map[new_r][new_c]) >= 4:
                return turn_count
        turn_count += 1

    return -1


print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다

start_horse_location_and_directions = [
    [0, 1, 0],
    [1, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
print("정답 = 9 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))

start_horse_location_and_directions = [
    [0, 1, 0],
    [0, 1, 1],
    [0, 1, 0],
    [2, 1, 2]
]
print("정답 = 3 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))

