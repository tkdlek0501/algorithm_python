# Q. 땅따먹기

# <문제분석>
# 총 N행 4열로 이루어져 있고
# 모든 칸에는 점수가 쓰여 있다
# 1행부터 땅을 밟으면 한 행씩 내려올 때,
# 각 행의 4칸 중 한 칸만 밟으면서 내려와야 한다
# *단, 한 행씩 내려올 때, 같은 열을 연속해서 밟을 수는 없다

# ex.
# 1 2 3 5
# 5 6 7 8
# 4 3 2 1

# 1행 4열 (5)
# 2행 에서는 4열 제외하고 3열 (7)
# 3행에서는 3열 제외하고 1열 (4)
# 행의 개수 N: 100,000 이하
# 열은 4개
# 땅(land)은 2차원 배열

# <풀이>
# 1. 행의 개수만큼 돈다
# 2. 이전에 방문한 열을 기억하고 있어야 한다
# 3. 이전에 방문한 열의 값을 제외하고 sort? or max?
# 4. 가장 큰 값만 넣으면 된다
# 그러나 전체적으로 봤을 때는 최선의 수가 아닐 수 있다
# 다음 같은 열에 더 큰 값이 있을 때 고르지를 못한다
# DP로 풀어야 한다
# 결국 모든 행을 거쳐서 가장 큰 수를 뽑아야 하므로
# 다음 행에서 이전 행의 같은 열을 제외한 값들 중 가장 큰 값을 누적해서
# 마지막에 다다르면 max 로 뽑아낼 수 있다

def solution(land):
    n = len(land)  # 행의 개수

    for i in range(1, n):  # 두 번째 행부터 시작
        for j in range(4):  # 열은 항상 4개
            # 이전 행에서 현재 열을 제외한 가장 큰 값을 더함
            land[i][j] += max(land[i-1][k] for k in range(4) if k != j)

    return max(land[-1])  # 마지막 행에서 가장 큰 값이 정답

# <피드백>
# 그리디는 현재의 최선을 선택하고,
# - 미래에 영향을 끼치지 않는다면
# DP는 미래의 최선을 만들기 위해 지금을 설계한다.
# - 미래에 영향을 끼친다면
# -> 여기서는 이전 열을 다음 행에서 쓰지 못하게 된다
# dp[i][j] = i행의 j열까지 밟았을 때 최대 점수
# 점화식
# dp[i][j] = max(dp[i-1][k] for k ≠ j) + land[i][j]