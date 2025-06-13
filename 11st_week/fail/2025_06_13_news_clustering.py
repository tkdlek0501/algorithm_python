# Q. 뉴스 클러스터링

# <문제분석>
# 기사의 제목을 기준으로 '블라인드 전형'
# '코딩 테스트' 각각 주목하는 기사로 나뉜다
# 이를 각각 묶어서 보여주고 싶다

# 묶는 기준을 정하기 위해서
# 집합 A, B 사이의 자카드 유사도 J(A, B) 는 두 집합의 교집합 크기를
# 두 집합의 합집합 크기로 나눈 값으로 정의된다

# ex.
# A = {1, 2, 3}
# B = {2, 3, 4}
# A n B = {2, 3}
# A u B = {1, 2, 3, 4}
# -> 2 / 4 = 0.5
# A와 B 모두 공집합일 경우에는 J(A, B) = 1 로 정의한다

# 다중집합
# A = {1, 1, 1}
# B = {1, 1, 1, 1, 1}
# A n B = 3개 (min(3, 5))
# A u B = 5개 (max(3, 5))

# A = {1, 1, 2, 2, 3}
# B = {1, 2, 2, 4, 5}
# A n B = {1, 2, 2}
# A u B = {1, 1, 2, 2, 3, 4, 5} # 1 등 이 2개 들어간다
# J(A, B) = 3/7

# 'FRANCE'
# 'FRENCH'
# 두 글자씩 끊어서 다중집합
# {FR, RA, AN, NC, CE}
# {FR, RE, EN, NC, CH}
# A n B = {FR, NC}
# A u B = {FR, RA, AN, NC, CE, RE, EN, CH}

# str1, str2 ; 길이는 2이상 1,000 이하
# 두 글자씩 끊어서 다중집합의 원소로 만든다 이때 영문자만 유효하고 기타공백이나 특수문자 포함되면 제거한다
# 다중집합 원소 사이를 비교할 때 대문자, 소문자 차이는 무시한다

# <풀이>
# 1. 두 글자씩 끊어서 알파벳이면 uppercase 로 만들어서 다중집합으로 만든다
# 2. 두 문자열의 자카드 유사도를 출력

from collections import Counter


def solution(str1, str2):
    arr1 = []
    for i in range(0, len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            arr1.append((str1[i].upper(), str1[i + 1].upper()))
    arr2 = []
    for i in range(0, len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            arr2.append((str2[i].upper(), str2[i + 1].upper()))

    counter1 = Counter(arr1)
    counter2 = Counter(arr2)

    inter = counter1 & counter2
    union = counter1 | counter2

    inter_count = sum(inter.values())
    union_count = sum(union.values())

    if union_count == 0:
        return 65536

    return int(inter_count / union_count * 65536)

# <피드백>
# 교집합과 합집합을 구하는 방법은 Couter를 이용해서 구할 수 있다
# 교집합은 counter1 & counter2
# 합집합은 counter1 | counter2

# 이 결과를 sum(inter.values()) 하면 합계를 구할 수 있다