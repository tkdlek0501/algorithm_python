# Q. 프렌즈4블록

# <문제분석>
# 같은 모양의 블록이 2 x 2 형태로 4개가 붙어있으면 사라지면서 점수 얻음
# 같은 블록은 여러 2 x 2 에 포함될 수 있다
# 조건에 만족하면 한꺼번에 지워진다

# 블록이 지워지면 위에 있는 블록이 아래로 떨어져 빈 공간을 채운다

# 입력으로 블록의 첫 배치가 주어지면 지워지는 블록은 모두 몇 개인지 판단
# 판의 높이 m, 폭 n과 판의 배치 정보 board 가 들어온다
# 2 < n, m <= 30
# board는 길이 n인 문자열 m개의 배열로 주어진다

# <풀이>
# 판을 2차원 배열로 생각?
# 모든 2 * 2 공간을 보면서 지워지는 행렬 저장
# 그 행렬 위치의 값을 지우고
# 블록이 아래로 떨어지는 처리
# 다시 모든 2 * 2 공간을 보면서 지워지는 행렬 저장

def solution(m, n, board):  # 높이, 폭, 배치정보
    answer = 0

    # 게임판
    game_map = [[[] for _ in range(n)] for _ in range(m)]

    # 게임판 데이터 만들기
    for i in range(m):
        for j in range(n):
            game_map[i][j] = board[i][j]

    while True:
        deleted = set()

        # 2x2 블록 찾기
        for i in range(0, m - 1):
            for j in range(0, n - 1):
                if game_map[i][j] == '0':  # 제거한 것이 포함돼 있으면 스킵
                    continue
                a = game_map[i][j]
                b = game_map[i][j + 1]
                c = game_map[i + 1][j]
                d = game_map[i + 1][j + 1]
                if a == b == c == d:
                    deleted.add((i, j))
                    deleted.add((i, j + 1))
                    deleted.add((i + 1, j))
                    deleted.add((i + 1, j + 1))

        # 2x2 블록 없으면 끝
        if not deleted:
            break

        # 지우기
        for x, y in deleted:
            game_map[x][y] = '0'
            answer += 1

        # 블록 내리기
        for j in range(n):  # 열 단위로
            temp = []
            for i in range(m - 1, -1, -1):  # 아래에서 위로 스캔
                if game_map[i][j] != '0':
                    temp.append(game_map[i][j])  # 남아 있는 블록 수집
            for i in range(m - 1, -1, -1):  # 다시 아래서부터
                if temp:  # 남겨둔 것
                    game_map[i][j] = temp.pop(0)  # 쌓인 블록을 하나씩 내려놓음
                else:
                    game_map[i][j] = '0'  # 남은 건 빈칸으로

    return answer

# <피드백>
# 1. 2x2 블록을 찾고 -> set 으로 중복 제거하며 관리 + '0' 은 무시
# 2. 2x2 블록이 없으면 끝 -> break 로 빠져나오기
# 3. 2x2에 해당하는 블록 지우기 -> '0' 으로 채우기
# -> 여기 까지는 어느 정도 풀었는데
# 4. 블록 내리기
# -> 제거한 것들은 '0'으로 채워놨으니, '0' 제외하고
# 열을 돌면서 그 줄을 아래에서 위로 스캔해서 남아있는 블록을 수집 후
# 다시 아래에서 위로 스캔해서 수집한 순서대로 꺼내서 넣어주면 됨