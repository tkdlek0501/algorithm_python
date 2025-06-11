# Q. 할인 행사

# <문제분석>
# 일정 금액 지불 시 10일 동안 회원 자격
# 매일 한 가지 제품을 할인
# 하루에 하나씩만 구매할 수 있다
# 원하는 제품과 수량이 할인하는 날짜와 10일 연속으로 일치할 경우에 맞춰서 회원가입 하려함

# ex. 바나나 3개, 사과 2개, 쌀 2개, 돼지고기 2개, 냄비 1개
# 14일 치킨, 사과, 사과, 바나나, 쌀, 사과, 돼지보기, 바나나, 돼지고기, 쌀, 냄비, 바나나, 사과, 바나나
# 셋째 날, 넷째 날, 다섯째 날 부터 수량 일치라서 회원가입 하려 한다

# 원하는 제품을 나타내는 문자열 want
# 원하는 제품 수량 나타내는 정수 배열 number
# 할인하는 제품 discount

# <풀이>
# 1. want와 number가 같으므로 zip 으로 dictionary 만들기
# 2. 하루하루 지나가면서 수량 충분한지 체크 - Counter 쓰기?
# 3. 같은지 비교 - sort 한 뒤 비교?

from collections import Counter


def solution(want, number, discount):
    answer = 0

    want_dic = {}
    for w, n in zip(want, number):
        want_dic[w] = want_dic.get(w, 0) + n

    for n in range(len(discount)):  # 할인 배열 시작 인덱스
        dis = discount[n: n + 10]  # 앞으로 10일 까지
        dis_dic = Counter(dis)
        for wd in want_dic:
            if not dis_dic[wd] or dis_dic[wd] < want_dic[wd]:  # 없거나 개수가 적으면 다음날로 이동
                break
        else:
            answer += 1

    return answer

# <피드백>
# 전체 시간 복잡도: O(N × K)
# (N = discount 길이, K = want 배열 길이 ≤ 10 → 거의 상수)

from collections import Counter
def solution(want, number, discount):
    answer = 0
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]

    for i in range(len(discount)-9):
        if dic == Counter(discount[i:i+10]):
            answer += 1

    return answer


from collections import Counter

def solution1(want, number, discount):
    answer = 0

    # 원하는 물품과 수량을 딕셔너리로 구성
    want_dict = dict(zip(want, number))

    for i in range(len(discount) - 9):  # 10일 연속 구간이므로 범위는 -9까지만
        # 현재 10일치 할인 목록
        window = discount[i:i+10]
        window_counter = Counter(window)

        # 원하는 모든 물품이 해당 기간에 만족하는지 확인
        for item in want_dict:
            if window_counter[item] < want_dict[item]:
                break
        else:
            answer += 1  # 모든 품목이 만족할 때만 카운트

    return answer