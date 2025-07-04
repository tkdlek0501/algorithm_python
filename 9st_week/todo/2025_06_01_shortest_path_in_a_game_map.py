from collections import deque


def solution(maps):
    answer = -1

    n_index = len(maps) - 1
    m_index = len(maps[0]) - 1

    # 동서남북 이동
    direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    # 캐릭터의 현재 위치 정보
    queue = deque([(0, 0, 1)])  # y, x, count

    while queue:
        cy, cx, count = queue.popleft()  # 현재 위치 및 횟수

        if cy == n_index and cx == m_index:
            return count

        for dy, dx in direction:
            ny = cy + dy
            nx = cx + dx

            if ny >= 0 and nx >= 0 and ny <= n_index and nx <= m_index and maps[ny][nx] == 1:  # 맵 밖이 아니고 벽이 없으면
                maps[ny][nx] = 0  # visited
                queue.append((ny, nx, count + 1))

    return answer

# 피드백
# dfs, 동서남북이동, visited 관리, 조건절
# 각각의 체크만 잘하면 된다
# 튜플 데이터를 넣을 때는 [()] 로 감싸서 넣기 주의하자