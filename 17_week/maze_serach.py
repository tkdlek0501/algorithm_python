# Q. 미로 탐색

# N x M 크기의 배열로 표현되는 미로가 있다
# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다.
# 이러한 미로가 주어졌을 때, (1, 1) 에서 출발하여 (N, M)의 위치로 이동할 때
# 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오.
# 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
# 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

# 입력
# 첫째 줄에 두 정수 N, M(2<=N, M<=100) 이 주어진다.
# 다음 N개의 줄에는 M개의 정수로 미로가 주어진다.
# 각각의 수들은 붙어서 입력으로 주어진다.

# 출력
# 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다.
# 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

# <문제 풀이>
# 미로이고 출발->도착인 최소의 칸 수를 출력해야 하므로
# BFS
# 이미 지나갔던 칸을 0으로 바꾸면서 진행하고 (visited 대신)
# 상하좌우 이동 가능 & N x M 내에서 진행 가능

from collections import deque
def solution(n, m, arr): # N, M, 2차원 배열
    answer = 0

    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque([(0, 0, 1)]) # x, y, count
    arr[0][0] = 0

    while queue:
        x, y, count = queue.popleft()

        if x == (n - 1) and y == (m - 1): # 도착
            return count

        for nx, ny in direction:
            dx = x + nx
            dy = y + ny
            if 0 <= dx < n and 0 <= dy < m:
                if arr[dx][dy] == 1:
                    arr[dx][dy] = 0 # 지나감 표시
                    queue.append((dx, dy, count + 1)) # 다음 칸

    return answer

if __name__  == "__main__":
    n, m = map(int, input().split())

    arr = [list(map(int, list(input().strip()))) for _ in range(n)]

    print(solution(n, m, arr))

# 예제
# 4 6
# 101111
# 101010
# 101011
# 111011
# -> 15

# 4 6
# 110110
# 110110
# 111111
# 111101
# -> 9

# 2 25
# 1011101110111011101110111
# 1110111011101110111011101
# -> 38

# 7 7
# 1011111
# 1110001
# 1000001
# 1000001
# 1000001
# 1000001
# 1111111
# -> 13