# Q. 숫자 변환하기

# <문제분석>
# 자연수 x를 y로 변환
# 1. x 에 n 을 더한다
# 2. x 에 2 를 곱한다
# 3. x 에 3 을 곱한다

# x, y, n 이 주어지면
# x 를 y 로 변환하기 위해 필요한 최소 연산 횟수를 return 하도록 한다
# x 를 y 로 만들 수 없다면 -1을 return
# 1 <= x <= y <= 1,000,000
# 1 <= n < y

# <풀이>
# 3가지 방법을 통해 최단으로 연산해야 한다
# BFS : queue에 (현재 값, 연산 횟수)
# while은 queue 가 없어질 때 까지
# visited 관리해서 중복 연산 방지

from collections import deque


def solution(x, y, n):
    queue = deque([(x, 0)])  # 현재 값, 연산 횟수

    visited = set()
    visited.add(x)

    while queue:
        current, count = queue.popleft()

        if current == y:
            return count

        for next_value in (current + n, current * 2, current * 3):
            if next_value <= y and next_value not in visited:
                visited.add(next_value)
                queue.append((next_value, count + 1))

    return -1

# <피드백>
# visited 로 중복연산을 제거해야 시간 초과에 걸리지 않는다
# BFS 에서 visited 는 웬만하면 필요하다

from collections import deque


def my_solution(x, y, n):
    answer = -1

    queue = deque([(x, 0)])  # 현재 값, count 으로 초기화
    visited = set()

    while queue:
        current, count = queue.popleft()

        # 같으면 count 반환
        if current == y:
            return count

        visited.add(current)

        # 아직 도달하지 못한 것 + visited에 있는 것만 queue에 넣어주기
        for next in ([current + n, current * 2, current * 3]):
            if next <= y and next not in visited:
                queue.append((next, count + 1))

    return answer