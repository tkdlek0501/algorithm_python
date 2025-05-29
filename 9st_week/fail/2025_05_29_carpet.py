# Q. 카펫
#
# 문제 설명
# Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.
#
# carpet.png
#
# Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.
#
# Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# 갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
# 노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
# 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.
# 입출력 예
# brown	yellow	return
# 10	2	[4, 3]
# 8	1	[3, 3]
# 24	24	[8, 6]


# <문제분석>
# 갈색 격자의 수 brown
# 노란색 격자의 수 yellow
# 가로, 세로 크기를 순서대로 배열에 담아 return
# 가로 >= 세로

# ex. brown 10 / yellow 2
# 노란색 2개를 갈색이 감싸야 한다
# ㅇ ㅇㅇ ㅇ
# ㅇ ㅁㅁ ㅇ
# ㅇ ㅇㅇ ㅇ
# 2개를 감싸기 위해서는 가로 길이는 2배? x
# 감싸기 위해서 필요한 개수?
# 1개 -> 3개
# 2개 -> 4개
# 3개 -> 5개
# => 즉 +2개 필요

# 근데 24 / 24 가 가능
#  o o o  o o  o  o o
#    ㅁ ㅁ ㅁ ㅁ ㅁ ㅁ
# 노란색 2줄도 가능하다

# 입출력 패턴
# brown + yellow = 가로 x 세로
# 곱하는 두 수는 가장 가까운 값, 즉 차이가 적은 값

def solution(brown, yellow):
    answer = []

    a = 0  # 가로
    b = 0  # 세로
    # a * b = brown + yellow

    # for 문 범위?
    sum_by = brown + yellow
    # 곱해서 sum 값을 만들 수 있는 값 찾기
    possible_comb = []
    for num in range(1, sum_by + 1):
        if sum_by % num == 0:
            possible_comb.append((num, int(sum_by / num)))
    idx = len(possible_comb) // 2
    a, b = possible_comb[idx]

    answer.append(a)
    answer.append(b)

    return answer

# 피드백
# 입출력 패턴으로 부터 규칙을 얻은 것은 좋으나
# +2가 된다는 조건도 고려를 충분히 했어야 했음
# 패턴을 만들 수 있는 모든 조건이 만족하지 못함
# 테두리는 언제나 한 줄이 되어야 함
# 즉 yellow 개수는 전체 격자의 크기와 비교 했을 때
# (가로 - 2) * (세로 - 2) = yellow
# 위 조건을 만족해야 함

def solution1(brown, yellow):
    total = brown + yellow

    for height in range(3, total):  # 최소 세로는 3부터
        if total % height == 0:
            width = total // height
            if width < height:
                continue  # 가로 ≥ 세로 조건
            if (width - 2) * (height - 2) == yellow:
                return [width, height]