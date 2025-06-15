# Q. 연속 부분 수열 합의 개수

# <문제분석>
# 수열
# 어떤 자연수로 이루어진 원형 수열의 연속하는 부분 수열의 합으로 만들 수 있는 수가 몇 가지인지
# 처음과 끝이 연결된 형태의 수열
# ex. [7, 9, 1, 1, 4]

# elements 가 순서대로 주어지면
# 연속 부분 수열의 합으로 만들 수 있는 수의 개수를 return

# elements 길이 <= 1,000
# elements 원소 <= 1,000

# 모든 수열 구해서 -> permutations?
# 그냥 수열이 아니라 연속해야 한다 permutaions 로 풀 수 없다
# 직접 수열을 만드려면
# 1) 1개씩
# 2) 2개씩 묶어서 합 넣어보기 이때 elements는 2배
# 합을 구해야 하고 중복 제거

def solution(elements):
    sum_set = set()

    extends = elements * 2  # 2배로 늘리고

    for n in range(1, len(elements) + 1):  # 1개부터 길이만큼
        for k in range(len(elements)):  # 시작 인덱스
            sum_set.add(sum(extends[k:k + n]))

    return len(sum_set)


def solution1(elements):
    ways = set()
    elements_copy = elements * 2

    for i in range(0, len(elements)):  # i번째 부터
        hap = 0
        for j in range(0, len(elements)):  # j개의 합
            hap += elements_copy[i + j]
            ways.add(hap)

    return len(ways)