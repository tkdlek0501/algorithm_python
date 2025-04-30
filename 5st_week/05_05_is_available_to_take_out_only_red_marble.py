# 스타트링크에서 판매하는 어린이용 장난감 중에서 가장 인기가 많은 제품은 구슬 탈출이다.
# 구슬 탈출은 직사각형 보드에 빨간 구슬과 파란 구슬을 하나씩 넣은 다음, 빨간 구슬을 구멍을 통해 빼내는 게임이다.
#
# 보드의 세로 크기는 N, 가로 크기는 M이고, 편의상 1×1크기의 칸으로 나누어져 있다.
# 가장 바깥 행과 열은 모두 막혀져 있고, 보드에는 구멍이 하나 있다.
# 빨간 구슬과 파란 구슬의 크기는 보드에서 1×1크기의 칸을 가득 채우는 사이즈이고,
# 각각 하나씩 들어가 있다. 게임의 목표는 빨간 구슬을 구멍을 통해서 빼내는 것이다. 이때, 파란 구슬이 구멍에 들어가면 안 된다.
#
# 이때, 구슬을 손으로 건드릴 수는 없고, 중력을 이용해서 이리 저리 굴려야 한다.
# 왼쪽으로 기울이기, 오른쪽으로 기울이기, 위쪽으로 기울이기, 아래쪽으로 기울이기와 같은 네 가지 동작이 가능하다.
#
# 각각의 동작에서 공은 동시에 움직인다. 빨간 구슬이 구멍에 빠지면 성공이지만,
# 파란 구슬이 구멍에 빠지면 실패이다. 빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다.
# 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다. 또, 빨간 구슬과 파란 구슬의 크기는 한 칸을 모두 차지한다.
# 기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지이다.
#
# 보드의 상태가 주어졌을 때, 10번 이하로 빨간 구슬을 구멍을 통해 빼낼 수 있는지 구하는 프로그램을 작성하시오.

# 입력
# 보드를 나타내는 2차원 배열 game_map이 주어진다.
# 이 때, 보드의 행, 열의 길이는 3이상 10 이하다.
#
# 보드 내에 문자열은 '.', '#', 'O', 'R', 'B' 로 이루어져 있다.
# '.'은 빈 칸을 의미하고,
# '#'은 공이 이동할 수 없는 장애물 또는 벽을 의미하며,
# 'O'는 구멍의 위치를 의미한다.
# 'R'은 빨간 구슬의 위치,
# 'B'는 파란 구슬의 위치이다.
#
# 입력되는 모든 보드의 가장자리에는 모두 '#'이 있다. 구멍의 개수는 한 개 이며, 빨간 구슬과 파란 구슬은 항상 1개가 주어진다.
#
# 출력
# 파란 구슬을 구멍에 넣지 않으면서 빨간 구슬을 10번 이하로 움직여서 빼낼 수 있으면 True, 없으면 False를 반환한다.

# <문제분석>
# 1. 보드는 세로는 N 가로는 M 의 사이즈이다
# 2. 편의상 1x1 크기의 칸으로 나눠져 있다
# 3. 가장 바깥 행과 열은 막혀져 있고 보드에는 하나의 구멍이 있다
# 4. 구슬의 크기는 1x1
# 5. *빨간 구슬을 구멍으로 넣는 것이 목표이다 파란 구슬은 들어가면 안된다 + 동시에 빠져도 안된다
# 6. *동작) 네가지 동작이 가능하다 : 왼, 오, 위, 아래 한 방향으로 기울이기 + 더 이상 구슬이 움직이지 않을 때 까지
# 7. 구슬은 동시에 같은 칸에 있을 수 없다
# 조건) 보드의 상태가 주어졌을 때 10번 이하로 성공할 수 있는지를 구해야 한다
# 보드의 행, 열의 길이는 3 이상 10 이하
# '.' : 빈 칸
# '#' : 장애물 -> 가장자리에는 모두 '#'이 있다
# '0' : 구멍의 위치 -> 1개이다
# 'R' : 빨간 구슬 -> 1개
# 'B' : 파란 구슬 -> 1개

# <문제풀이>
# 4가지 동작 중 어떤 동작이 유리한지 모른다 모든 경우의 수를 알아야 한다
# -> 모든 수를 탐색해도 괜찮은 범위
# 구슬은 한 방향으로만 이동해서 #이나 0에 도달할 때까지 이동할 수 있다 + 각 구슬 전까지
# 맨 가장자리는 항상 '#' 장애물 이니까 가장 자리를 제외해도 되지 않을까?
# 매 턴 각 구슬이 어디까지 이동하는지 봐야 한다

# <구현>
# for 이번 턴 in 10번 턴 or while 10번 턴?
#    for 각 방향 x -> BFS
# 빨간 구슬을 그 방향으로 한칸 씩 쭉 이동
# 파란 구슬을 그 방향으로 한칸 씩 쭉 이동
#      BFS 로 4가지 방향에 대해 10번 반복
# 그 중에 빨간색이 들어가는 경우가 있다면 성공 아니면 실패니까 break return 으로 빠져나오기
# 보통 BFS에서 Queue는 visited 용도로 저장했는데
# 이 문제에서는 visited 4차원 배열로 저장
# -> [red_row][red_col][blue_row][blue_col] = True 로 관리

from collections import deque

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]

# 방향성 구현
# 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 다음 이동이 벽이거나 혹은 현재 위치가 구멍이라면
def move_until_wall_or_hole(r, c, diff_r, diff_c, game_map):
    move_count = 0
    while game_map[r + diff_r][c + diff_c] != '#' and game_map[r][c] != 'O':
        r += diff_r
        c += diff_c
        move_count += 1
    return r, c, move_count

def is_available_to_take_out_only_red_marble(game_map):
    n, m = len(game_map), len(game_map[0])
    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    queue = deque()
    red_row, red_col, blue_row, blue_col = -1, -1, -1, -1
    for i in range(n):
        for j in range(m):
            if game_map[i][j] == "R":
                red_row, red_col = i, j
            elif game_map[i][j] == "B":
                blue_row, blue_col = i, j

    queue.append((red_row, red_col, blue_row, blue_col, 1))
    visited[red_row][red_col][blue_row][blue_col] = True

    while queue:
        red_row, red_col, blue_row, blue_col, try_count = queue.popleft()  # FIFO
        if try_count > 10:  # 10 이하여야 한다.
            break

        for i in range(4):
            next_red_row, next_red_col, r_count = move_until_wall_or_hole(red_row, red_col, dr[i], dc[i], game_map)
            next_blue_row, next_blue_col, b_count = move_until_wall_or_hole(blue_row, blue_col, dr[i], dc[i], game_map)

            if game_map[next_blue_row][next_blue_col] == 'O':  # 파란 구슬이 구멍에 떨어지지 않으면(실패 X)
                continue
            if game_map[next_red_row][next_red_col] == 'O':  # 빨간 구슬이 구멍에 떨어진다면(성공)
                return True
            if next_red_row == next_blue_row and next_red_col == next_blue_col:  # 빨간 구슬과 파란 구슬이 동시에 같은 칸에 있을 수 없다.
                if r_count > b_count:  # 이동 거리가 많은 구슬을 한칸 뒤로
                    next_red_row -= dr[i]
                    next_red_col -= dc[i]
                else:
                    next_blue_row -= dr[i]
                    next_blue_col -= dc[i]
            # BFS 탐색을 마치고, 방문 여부 확인
            if not visited[next_red_row][next_red_col][next_blue_row][next_blue_col]:
                visited[next_red_row][next_red_col][next_blue_row][next_blue_col] = True
                queue.append((next_red_row, next_red_col, next_blue_row, next_blue_col, try_count + 1))

    return False


print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다



game_map = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", "O", ".", ".", ".", ".", "R", "B", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = False / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))


game_map = [
["#", "#", "#", "#", "#", "#", "#"],
["#", ".", ".", "R", "#", "B", "#"],
["#", ".", "#", "#", "#", "#", "#"],
["#", ".", ".", ".", ".", ".", "#"],
["#", "#", "#", "#", "#", ".", "#"],
["#", "O", ".", ".", ".", ".", "#"],
["#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = True / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))