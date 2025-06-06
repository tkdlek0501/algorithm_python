# 중앙에 노란색 테두리 1줄은 갈색
# 격자의 개수는 알지만 전체 크기 모름
# 갈색 격자의 수 brown, 노란색 격자의 수 yellow 주어지면
# 가로, 세로 크기를 순서대로 배열에 담아 retur

# 8 <= brown <= 5,000
# 1 <= yellow <= 2,000,000
# 가로 길이 >= 세로 길이

# <풀이>
# 가운데에 노란색이 존재하고 갈색은 1줄 이니까
# 갈색 세로 = 노란색 세로 + 2
# 갈색 가로 = 노란색 가로 + 2
# (세로 - 2) * (가로 - 2) = 노란색 개수

# 10, 2 면 4, 3
# 8, 1 이면 3, 3
# 24, 24 이면 8, 6
# 즉 10 + 2 = 4 * 3
# 8 + 1 = 3 * 3
# 24 + 24 = 8 * 6 
# 으로 표현됨

def solution(brown, yellow):  # 10, 2 -> [4, 3]
    answer = [0, 0]

    sum_val = brown + yellow
    for x in range(1, sum_val + 1):  # 가로길이
        if sum_val % x == 0:
            y = sum_val // x

        if x >= y and (x - 2) * (y - 2) == yellow:
            return [x, y]

    return answer