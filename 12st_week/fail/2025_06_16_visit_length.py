# Q. 방문 길이

# <문제분석>
#  4가지 명령어를 통해 움직일 수 있다
# U : 위로 한 칸
# D : 아래로 한 칸
# R : 오른쪽으로 한 칸
# L : 왼쪽으로 한 칸

# 캐릭터는 좌표평면 (0, 0) 위치에서 시작
# 좌표평면의 경계는
# 왼쪽 위 (-5, 5)
# 왼쪽 아래 (-5, 5)
# 오른쪽 위 (5, 5)
# 오른쪽 아래 (5, -5)
# 5 * 5

# 게임 캐릭터가 지나간 길 중 캐릭터가 처음 걸어본 길의 길이를 구하려고 한다
# -> 간선을 기억하고 있어야 한다
# 같은 길로는 가지 않아야 한다 - visited
# *단, 좌표 평면의 경계를 넘어가는 명령어는 무시해야 한다

# def solution(dirs):  # 명령어 배열
#     answer = 0
#
#     # 명령어
#     dic = {}
#     dic['U'] = (1, 0)
#     dic['D'] = (-1, 0)
#     dic['R'] = (0, 1)
#     dic['L'] = (0, -1)
#
#     visited = [(0, 0)]  # 지나온 좌표
#     current_position = (0, 0)  # 현재 위치
#     # 처음 걸어본 길의 길이 (1씩만 움직임)
#     for dir in dirs:
#         nx = current_position[0] + dic[dir][0]
#         ny = current_position[1] + dic[dir][1]
#
#         if -5 <= nx <= 5 and not -5 <= ny <= 5 and not (nx, ny) in visited:
#             visited.append((nx, ny))
#             current_position = (nx, ny)
#             answer += 1
#
#     return answer

def solution(dirs):
    move = {
        'U': (0, 1),
        'D': (0, -1),
        'R': (1, 0),
        'L': (-1, 0)
    }

    x, y = 0, 0
    visited = set()
    answer = 0

    for d in dirs:
        dx, dy = move[d]
        nx, ny = x + dx, y + dy

        # 범위 체크
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            path = ((x, y), (nx, ny))
            reverse_path = ((nx, ny), (x, y))
            if path not in visited and reverse_path not in visited:
                visited.add(path)
                visited.add(reverse_path)
                answer += 1
            x, y = nx, ny

    return answer

# <피드백>
# dictionary 에 초기화할 떄
# dic {
#    'A' : value,
#    'B' : value2
# }
# 에 익숙해지자

# 이 문제에서는 방문 좌표가 아니라 방문 간선을 중복하지 마라 했으므로
# 중복 제거에는 set() 이 바람직하고
# 간선은 정방향과 역방향을 모두 visited 에서 관리해주어야 한다
