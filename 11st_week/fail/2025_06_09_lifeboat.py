# Q. 구명보트

# <문제분석>
# 구명보트에 1. 한 번에 최대 2명씩 탈 수 있고
# 2. 무게 제한이 있다

# ex. 몸무게 [70, 50, 80, 50]
# 무게 제한 100 이면
# 2번째와 4번째 사람은 같이 탈 수 있고 1, 3은 같이 못 탐
# 구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 한다
# -> 적게? 최소로 목표에 도달하려면 bfs?
# 몸무게 배열 people,
# 무게 제한 limit
# 모든 사람을 구출하기 위해 필요한 구명보트 개수 최솟값 return

# <풀이>
# 순서는 상관없고 근데 유리하게 가져가려면 100을 딱 맞추는 게 중요
# 이걸 계산할 수는 없으니 경우의 수를 다 뿌려야 한다?
# 최대 한 번에 2명씩 이니까 순열 이용? 4명에 대한 순열로 앞에서부터 태우면?

# from itertools import permutations
# from collections import deque


# def solution(people, limit):
#     # people에서 순열로 모든 조합 가져오기
#     queue = deque()
#     for p in permutations(people, len(people)):
#         queue.append(p)
#
#     min_count = len(people)
#     while queue:  # 조합마다 카운트 세기
#         q = queue.pop()  # [70, 50, 80, 50]
#         count = 1  # 구명보트 사용 횟수
#         sum_weight = 0  # 무게
#         peo = 0  # 인원 수
#
#         # 인원수 또는 무게 제한이 채워질 때마다 count += 1 해주기
#         for weight in q:
#             if limit < sum_weight + weight or 2 < peo + 1:
#                 count += 1
#                 sum_weight = 0
#                 peo = 0
#
#             sum_weight += weight
#             peo += 1
#
#         min_count = min(count, min_count)
#
#     return min_count

# <피드백>
# 제한이 1명이상 50,000 이하라서 permutations 못 씀
# 탐색으로 풀 수 없는 문제
# 짝을 짓는 문제이고 제한 범위가 넓다면
# -> 정렬 + greedy + 투포인터 사용

def solution(people, limit):
    people.sort()  # 정렬
    left = 0  # 가벼운 사람
    right = len(people) - 1  # 무거운 사람
    boats = 0  # 보트 수

    # 가장 무거운 사람과 가장 가벼운 사람을 짝 지어서 처리
    while left <= right:
        if people[left] + people[right] <= limit:  # limit 보다 작으면
            left += 1  # 같이 탐 (left + 1 처리)
        right -= 1  # 무거운 사람은 무조건 처리 (right - 1 처리)
        boats += 1

    return boats