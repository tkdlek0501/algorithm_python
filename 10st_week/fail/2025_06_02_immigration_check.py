# Q. 입국 심사
#
# 문제 설명
# n명이 입국심사를 위해 줄을 서서 기다리고 있습니다. 각 입국심사대에 있는 심사관마다 심사하는데 걸리는 시간은 다릅니다.
#
# 처음에 모든 심사대는 비어있습니다. 한 심사대에서는 동시에 한 명만 심사를 할 수 있습니다. 가장 앞에 서 있는 사람은 비어 있는 심사대로 가서 심사를 받을 수 있습니다. 하지만 더 빨리 끝나는 심사대가 있으면 기다렸다가 그곳으로 가서 심사를 받을 수도 있습니다.
#
# 모든 사람이 심사를 받는데 걸리는 시간을 최소로 하고 싶습니다.
#
# 입국심사를 기다리는 사람 수 n, 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 times가 매개변수로 주어질 때, 모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# 입국심사를 기다리는 사람은 1명 이상 1,000,000,000명 이하입니다.
# 각 심사관이 한 명을 심사하는데 걸리는 시간은 1분 이상 1,000,000,000분 이하입니다.
# 심사관은 1명 이상 100,000명 이하입니다.
# 입출력 예
# n	times	return
# 6	[7, 10]	28
# 입출력 예 설명
# 가장 첫 두 사람은 바로 심사를 받으러 갑니다.
#
# 7분이 되었을 때, 첫 번째 심사대가 비고 3번째 사람이 심사를 받습니다.
#
# 10분이 되었을 때, 두 번째 심사대가 비고 4번째 사람이 심사를 받습니다.
#
# 14분이 되었을 때, 첫 번째 심사대가 비고 5번째 사람이 심사를 받습니다.
#
# 20분이 되었을 때, 두 번째 심사대가 비지만 6번째 사람이 그곳에서 심사를 받지 않고 1분을 더 기다린 후에 첫 번째 심사대에서 심사를 받으면 28분에 모든 사람의 심사가 끝납니다.


def solution(n, times): # 심사받을 수, 심사관마다의 걸리는 시간
    left = 1
    right = max(times) * n # 가장 오래걸리는 경우 시간
    answer = right

    while left <= right:
        mid = (left + right) // 2 # 중간값 찾기
        total = sum(mid // time for time in times) # 모든 심사 시간으로 mid를 나누기 = 처리 가능한 수

        if total >= n:
            # 심사가 가능하므로 시간 줄여보기
            answer = mid
            right = mid - 1
        else:
            # 심사가 불가능하므로 시간 늘리기
            left = mid + 1

    return answer

# <피드백>
# 문제 설명은 장황하지만
# 이분 탐색을 이용하는 전형적인 최소 시간 찾기 문제이다
# 1. 탐색 대상이 정수 범위
# 2. 주어진 시간안에 몇 명 처리 가능한지 구할 수 있음
# 3. 판별 함수가 단조 증가 or 감소 (시간이 커질 수록 처리량 증가)
# -> 최소값/ 최대값 구하는 문제에서의 전형적인 패턴


# left, right 설정만 잘하면 풀기 어렵지 않다