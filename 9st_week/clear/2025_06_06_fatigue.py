# 0이상의 정수로 표현하는 피로도
# 각 던전마다 탐험을 시작하기 위해 필요한 '최소 필요 피로도'
# 던전 탐험 마치면 소모되는 '소모 피로도'

# 최대한 많이 탐험
# 현재 피로도 k
# 각 던전별 '최소피로도','소모 피로도' 2차원 배열 dungeons

# 어떤 순서로 해야 유리한지 모르기 때문에 경우의 수 다 해봐야 함

from itertools import permutations


def solution(k, dungeons):  # 현재 피로도, 던전 정보
    max_count = 0

    dungeon_arr = []
    for p in permutations(dungeons, len(dungeons)):
        dungeon_arr.append(p)

    for dungeon in dungeon_arr:
        current = k
        count = 0
        for need, use in dungeon:  # 던전 순서 배열
            if need <= current:  # 필요 피로도 충족
                current -= use  # 소모 피로도
                count += 1
            else:
                break
        max_count = max(max_count, count)

    return max_count

# <피드백>
# 최소 횟수라고 해서 BFS 로 접근하지 않아야 하는게
# 결국 모든 순서에 대해 해봐야 하므로(순열) 순서가 고정되지 않기 때문
# BFS는 미로 탈출이나 단어 변환 등에서 유리하다
