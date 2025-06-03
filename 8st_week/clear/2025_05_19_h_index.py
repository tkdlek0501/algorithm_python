# Q. H-Index
# 문제 설명
# H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.
#
# 어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.
#
# 어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# 과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
# 논문별 인용 횟수는 0회 이상 10,000회 이하입니다.
# 입출력 예
# citations	return
# [3, 0, 6, 1, 5]	3
# 입출력 예 설명
# 이 과학자가 발표한 논문의 수는 5편이고, 그중 3편의 논문은 3회 이상 인용되었습니다. 그리고 나머지 2편의 논문은 3회 이하 인용되었기 때문에 이 과학자의 H-Index는 3입니다.

# <문제분석>
# 논문 n 편
# h 번 이상 인용된 논문이 h편 이상이고
# 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 H-Index

# ex.
# [3, 0, 6, 1, 5] 라면
# 논문의 수는 5편(n)
# 그 중 3편의 논문은 3회 이상 인용되었다
# 그리고 나머지 2편의 논문은 3회 이하 인용 되었으므로
# H-Index는 3

# def solution(citations):
#     h_array = []
#
#     for h in citations:
#         if h > len(citations):
#             continue
#         over_h_count = 0
#         for i in citations:
#             if i >= h:
#                 over_h_count += 1
#         if over_h_count >= h:
#             h_array.append(h)
#     h_array.sort(reverse=True)
#
#     return h_array[0]

# <피드백>
# 문제 이해를 잘못했다.
# h 번은 주어진 배열 속에서만 검사하는 게 아니라
# 0부터 n까지 모든 수에 대해 고려해야 한다
# 논문의 수와 인용횟수는 다른 개념이다

# <아이디어> -> 아이디어 자체는 내가 생각한 것과 크게 다르지는 않다
# 1. 0부터 n까지 가능한 모든 h에 대해 검사
# 2. 각각에 대해 인용횟수가 h 이상인 논문 수를 세고
# 3. 그 수가 h 이상이면 후보로 간주
# 4. 그 중 가장 큰 h를 반환

# comprehesion 방식에 익숙해지자
# citaions를 돌아서 나온 c들 중 h 보다 크거나 같으면 1을 반환하고
# 그 값들을 sum 하는 거다(count 계산)
def solution(citations):
    n = len(citations) # 논문의 개수
    max_h = 0 # 인용된 수

    for h in range(0, n + 1):  # 0부터 n(논문의 수)까지 모든 h값 체크
        count = sum(1 for c in citations if c >= h)
        if count >= h:
            max_h = h  # 조건 만족하는 h 중 최대값 갱신

    return max_h
