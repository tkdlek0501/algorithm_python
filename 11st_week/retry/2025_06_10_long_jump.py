# Q. 멀리뛰기

# <문제분석>
# 한 번에 1칸 or 2칸을 뛸 수 있다
# ex.
# 칸이 총 4칸 있다면
# 1칸 x 4
# 1칸 2칸 1칸
# ...
# 5가지 방법

# 멀리뛰기할 칸의 수 n
# 끝에 도달하는 방법이 몇가지인지 알아내서
# 여기에 1234567을 나눈 나머지를 return

# <풀이>
# n 까지 도달하는 모든 방법의 수를 계산
# 1칸 or 2칸 움직이는 2가지 방법만 있음
# +1 하는 것과 +2 하는 것 재귀로 반복
# queue 를 이용해서 현재 위치만 관리?

# from collections import deque
#
# def solution(n):
#     ways = 0  # 방법의 수
#
#     queue = deque([0])  # 현재 위치
#
#     while queue:
#         q = queue.pop()  # 위치 0 부터 시작
#         if q == n:  # n 값에 정확히 도달하면
#             ways += 1
#         elif q < n:  # n 보다 작으면
#             queue.append(q + 1)
#             queue.append(q + 2)
#
#     return ways % 1234567

def solution(n):
    dp = [0] * (n + 1)  # 0부터 n까지 저장할 배열 생성 // dp[0] 은 사용 안하니까 + 1
    dp[1] = 1  # 첫 번째 값
    if n >= 2:
        dp[2] = 2  # 두 번째 값

    for i in range(3, n + 1): # 3부터 시작해서 n까지
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567  # 피보나치 점화식

    return dp[n]

# <피드백>
# 범위가 최대 2000 이라 재귀나 bfs 등으로 탐색할 수 없는 넓은 범위
# 방법의 수를 묻고 있고, 패턴화 시키면 이전 방법의 수의 합이 다음 방법의 수가 됨을 알 수 있음
# 즉 피보나치형 문제라고 볼 수 있다
# dp[n] = dp[n-1] + dp[n-2]