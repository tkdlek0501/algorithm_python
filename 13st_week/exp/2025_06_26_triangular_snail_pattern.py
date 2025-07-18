# Q. 삼각 달팽이

# <문제분석>
# 정수 n 이 매개변수로 주어짐
# 밑변의 길이와 높이가 n인 삼각형
# 맨 위부터 반시계 방향으로 달팽이 채우기 진행한 후
# 첫 행부터 마지막 행까지 모두 순서대로 합친 새로운 배열을 return 하도록 한다

# 1. 왼쪽 아래로 진행
# 2. 오른쪽으로 진행
# 3. 왼쪽 위로 진행
# 다시 왼쪽 아래로 진행
# 아래와 같이 표현해서 보면 된다
# []
# [] []
# [] [] []
# [] [] [] []

# n = 4 일 때 10개 1 2 3 4
# n = 5 일 때 15개 1 2 3 4 5
# n = 6 일 때 21개 1 2 3 4 5 6
# 등차수열 증가
# sum(i for i in range(1, n + 1))
# n * (n + 1) // 2

def solution(n):
    total = n * (n + 1) // 2  # 총 숫자 개수
    triangle = [[0] * (i + 1) for i in range(n)]

    x, y = 0, 0  # 시작 좌표
    num = 1
    direction = 0  # 0: 아래, 1: 오른쪽, 2: 왼쪽 위
    directions = [(1, 0), (0, 1), (-1, -1)]

    while num <= total:
        triangle[x][y] = num
        num += 1

        dx, dy = directions[direction]
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny <= nx and triangle[nx][ny] == 0:
            x, y = nx, ny
        else:
            # 방향 전환
            direction = (direction + 1) % 3
            dx, dy = directions[direction]
            x, y = x + dx, y + dy

    # 결과 1차원 배열로 펴기
    result = []
    for row in triangle:
        result.extend(row)

    return result

# <피드백>
# 1. 삼각형 만들기
#     [[0] * (i + 1) for i in range(n)]
# 2. 방향 구하기
# 3. total 값 구하기 -> 등차수열
#     n * (n + 1) // 2
# 4. 조건
#     if 0 <= nx < n and 0 <= ny <= nx and tri[nx][ny] == 0
# 5. 방향전환
#     direction = (direction + 1) % 3 (다음 방향)
# 6. 2차원 배열 1차원으로 펼치기
#     for row in triangle:
#         result.extend(row)