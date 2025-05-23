# Q. 더 맵게
#
# 문제 설명
# 매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.
#
# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
# Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.
#
# 제한 사항
# scoville의 길이는 2 이상 1,000,000 이하입니다.
# K는 0 이상 1,000,000,000 이하입니다.
# scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
# 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.
# 입출력 예
# scoville	K	return
# [1, 2, 3, 9, 10, 12]	7	2
# 입출력 예 설명
# 스코빌 지수가 1인 음식과 2인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.
# 새로운 음식의 스코빌 지수 = 1 + (2 * 2) = 5
# 가진 음식의 스코빌 지수 = [5, 3, 9, 10, 12]
#
# 스코빌 지수가 3인 음식과 5인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.
# 새로운 음식의 스코빌 지수 = 3 + (5 * 2) = 13
# 가진 음식의 스코빌 지수 = [13, 9, 10, 12]
#
# 모든 음식의 스코빌 지수가 7 이상이 되었고 이때 섞은 횟수는 2회입니다.


# <문제분석>
# 모든 음식의 스코빌 지수를 K이상으로 만들고 싶다
# 섞은 음식 지수 = 가장 맵지 않은 음식 지수 + (두번째로 맵지 않은 음식의 지수 * 2)
# 모든 음식의 지수가 K이상이 될 때까지 반복하여 섞는다
# 입력) 각 음식의 스코빌 지수 배열 scoville / 원하는 스코빌 지수 K
# 출력) 모든 음식의 스코빌 지수 K 이상으로 만들기 위해 섞어야 하는 최소 횟수 return

# <풀이>
# 제한) scoville 길이 2 이상 1,000,000 이하
# K는 0 이상 1,000,000,000 이하
# 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없으면 -1 return

# ex.
# 지수가 1과 2인 음식 섞으면 1 + (2 * 2) = 5
# 가진 음식의 스코빌 지수 = [1,2,3,9,10,12] -> [5,3,9,10,12]
# 가장 맵지 않은 음식과 두 번째 음식을 계속 섞는 과정이 필요 -> min_heap
# 섞은 횟수 = answer


import heapq


def solution(scoville, K):
    answer = 0

    min_heap = []

    # min_heap 초기화
    for sco in scoville:
        heapq.heappush(min_heap, sco)

    # min_heap에서 꺼내면서 K보다 작으면 다음 것과 섞기
    # 섞은 결과가 K보다 작으면 다시 min_heap에 그 값 넣기
    # 섞은 결과가 K보다 커지더라도 min_heap에 넣기
    # min_heap에 있는 모든 수가 K보다 커질 때까지 실행
    # -> 각 수가 K보다 큰지 어떻게 판단?
    # 하나라도 작으면 true로

    # 섞어서 커졌다라고 하더라도 넣어줘야 됨
    # 만약 이미 큰 애면? 얘도 넣어줘야 됨? 이것보다 작은게 없는 상황이니까 return

    while any(m < K for m in min_heap):
        min_k = heapq.heappop(min_heap)
        if min_k < K:
            if not min_heap: # 2개에서 1개가 되는 과정 반복하다가 K에 못미치는 1개 남은 상황
                return -1
            next_min = heapq.heappop(min_heap)
            mix = min_k + (next_min * 2)
            heapq.heappush(min_heap, mix)
            answer += 1

    return answer

# <피드백>
# heapq.heappush(arr, 추가할 요소) : min heap 에 요소 넣기
# heapq.heappop(arr) : 가장 작은 값 꺼내오기
# any() 를 쓰는 것은 조건에는 부합하지만 성능상 매 반복마다 실행해야 하기 때문에 좋지는 않다
#

import heapq as hq
def solution1(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K: # 최소값이 K보다 크다면 끝
            break
        if len(scoville) == 0: # 다음 것을 못 꺼내는 상황이면 -1
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1

    return answer