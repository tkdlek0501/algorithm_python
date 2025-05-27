# Q. 아이템 줍기
#
# 문제 설명
# 다음과 같은 다각형 모양 지형에서 캐릭터가 아이템을 줍기 위해 이동하려 합니다.
#
# rect_1.png
#
# 지형은 각 변이 x축, y축과 평행한 직사각형이 겹쳐진 형태로 표현하며, 캐릭터는 이 다각형의 둘레(굵은 선)를 따라서 이동합니다.
#
# 만약 직사각형을 겹친 후 다음과 같이 중앙에 빈 공간이 생기는 경우, 다각형의 가장 바깥쪽 테두리가 캐릭터의 이동 경로가 됩니다.
#
# rect_2.png
#
# 단, 서로 다른 두 직사각형의 x축 좌표 또는 y축 좌표가 같은 경우는 없습니다.
#
# rect_4.png
#
# 즉, 위 그림처럼 서로 다른 두 직사각형이 꼭짓점에서 만나거나, 변이 겹치는 경우 등은 없습니다.
#
# 다음 그림과 같이 지형이 2개 이상으로 분리된 경우도 없습니다.
#
# rect_3.png
#
# 한 직사각형이 다른 직사각형 안에 완전히 포함되는 경우 또한 없습니다.
#
# rect_7.png
#
# 지형을 나타내는 직사각형이 담긴 2차원 배열 rectangle, 초기 캐릭터의 위치 characterX, characterY, 아이템의 위치 itemX, itemY가 solution 함수의 매개변수로 주어질 때, 캐릭터가 아이템을 줍기 위해 이동해야 하는 가장 짧은 거리를 return 하도록 solution 함수를 완성해주세요.
#
# 제한사항
# rectangle의 세로(행) 길이는 1 이상 4 이하입니다.
# rectangle의 원소는 각 직사각형의 [좌측 하단 x, 좌측 하단 y, 우측 상단 x, 우측 상단 y] 좌표 형태입니다.
# 직사각형을 나타내는 모든 좌표값은 1 이상 50 이하인 자연수입니다.
# 서로 다른 두 직사각형의 x축 좌표, 혹은 y축 좌표가 같은 경우는 없습니다.
# 문제에 주어진 조건에 맞는 직사각형만 입력으로 주어집니다.
# charcterX, charcterY는 1 이상 50 이하인 자연수입니다.
# 지형을 나타내는 다각형 테두리 위의 한 점이 주어집니다.
# itemX, itemY는 1 이상 50 이하인 자연수입니다.
# 지형을 나타내는 다각형 테두리 위의 한 점이 주어집니다.
# 캐릭터와 아이템의 처음 위치가 같은 경우는 없습니다.
# 전체 배점의 50%는 직사각형이 1개인 경우입니다.
# 전체 배점의 25%는 직사각형이 2개인 경우입니다.
# 전체 배점의 25%는 직사각형이 3개 또는 4개인 경우입니다.
# 입출력 예
# rectangle	characterX	characterY	itemX	itemY	result
# [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]	1	3	7	8	17
# [[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]]	9	7	6	1	11
# [[1,1,5,7]]	1	1	4	7	9
# [[2,1,7,5],[6,4,10,10]]	3	1	7	10	15
# [[2,2,5,5],[1,3,6,4],[3,1,4,6]]	1	4	6	3	10
# 입출력 예 설명
# 입출력 예 #1
#
# rect_5.png
#
# 캐릭터 위치는 (1, 3)이며, 아이템 위치는 (7, 8)입니다. 위 그림과 같이 굵은 선을 따라 이동하는 경로가 가장 짧습니다.
#
# 입출력 예 #2
#
# rect_6.png
#
# 캐릭터 위치는 (9, 7)이며, 아이템 위치는 (6, 1)입니다. 위 그림과 같이 굵은 선을 따라 이동하는 경로가 가장 짧습니다.
#
# 입출력 예 #3
#
# rect_8.png
#
# 캐릭터 위치는 (1, 1)이며, 아이템 위치는 (4, 7)입니다. 위 그림과 같이 굵은 선을 따라 이동하는 경로가 가장 짧습니다.
#
# 입출력 예 #4, #5
#
# 설명 생략

from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    # 상, 하, 좌, 우 이동
    direction = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    # *테두리 구하기
    border = []  # (Y, X) 로 관리하기
    # 테두리는 직사각형들의 합친 모습으로 구해짐
    # rectangle : 좌측 하단 x/ y, 우측 상단 x/ y
    possible_root = []  # (Y, X)

    # queue랑 visited 관리
    queue = deque()  # 지금 위치(Y, X), 거리
    visited = set()

    # item 이랑 같은지 체크해서 return
    # visited 에 계속 넣어주기
    # 다음 가능한 위치 확인 (동서남북 중에 테두리 데이터에 있는지)
    queue.append((characterY, characterX, 0))
    visited.add((characterY, characterX))
    while queue:
        cY, cX, distance = queue.popleft()

        if cY == itemY and cX == itemX:
            return distance

        for dx, dy in direction:
            nY = cY + dy  # 다음 갈 곳
            nX = cX + dx  # 다음 갈 곳
            if (nY, nX) not in visited and (nY, nX) in possible_root:
                queue.append(nY, nX, distance + 1)
                visited.add((nY, nX))

    return answer

# <피드백>
# 공식 트릭임 – 이 문제는 유명한 "2배 좌표 확장 트릭" 문제
# 이 트릭을 모르는 상태에서 절대 못 풂
# “좌표계에서 겹침”, “테두리만 이동”, “모서리 분리 안 됨” → 이런 말이 나오면 “혹시 2배 확장인가?” 생각.
# 좌표*2, 내부: 2, 테두리: 1 마킹 → BFS → 결과 /2

def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[0]*102 for _ in range(102)]  # 2배 좌표이므로 최대 100*2 = 200 이상
    visited = [[0]*102 for _ in range(102)]

    # 1. 테두리 마킹
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1*2, y1*2, x2*2, y2*2
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1 < i < x2 and y1 < j < y2:
                    board[i][j] = 2  # 내부
                elif board[i][j] != 2:
                    board[i][j] = 1  # 테두리

    # 2. BFS
    q = deque()
    q.append((characterX*2, characterY*2, 0))  # 시작 위치 2배
    visited[characterX*2][characterY*2] = 1

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while q:
        x, y, dist = q.popleft()
        if x == itemX*2 and y == itemY*2:
            return dist // 2  # 거리도 2배였으므로 다시 2로 나눠줌

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < 102 and 0 <= ny < 102:
                if board[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny, dist+1))

    return 0