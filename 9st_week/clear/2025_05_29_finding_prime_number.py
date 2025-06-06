# Q. 소수 찾기
#
# 문제 설명
# 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
#
# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.
#
# 제한사항
# numbers는 길이 1 이상 7 이하인 문자열입니다.
# numbers는 0~9까지 숫자만으로 이루어져 있습니다.
# "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
# 입출력 예
# numbers	return
# "17"	3
# "011"	2
# 입출력 예 설명
# 예제 #1
# [1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.
#
# 예제 #2
# [0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.
#
# 11과 011은 같은 숫자로 취급합니다.


# <문제분석>
# 한자리 숫자가 적힌 종이 조각
# 흩어진 종이 조각 붙여서 소수 몇 개 만들 수 있는지 알아내야 함

# numbers 주어지면
# 그 걸로 만들 수 있는 소수가 몇 개 인지 return

# numbers 의 길이는 1이상 7이하
# numbers는 0~9까지 숫자만
# "013" 은 0, 1, 3 3개의 종이 조각

# ex.
# [1, 7] 이면 소수 [7, 17, 71] 만들 수 있음
# [0, 1, 1] 이면 [11, 101] 만들 수 있음 11과 011은 같은 숫자로 취급됨


# 풀이
# 1. 우선 numbers를 배열에 담기
# 2. 1의 자리, 10의 자리... 몇 자리로 쓸지?
# 3.

from itertools import permutations


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # 2 ~ n의 제곱근까지 판별하면 소수 구함
        if n % i == 0:
            return False
    return True


def solution(numbers):
    number_set = set()  # 중복 불가

    # 1자리 ~ len(numbers)자리까지 순열 생성
    for i in range(1, len(numbers) + 1):  # 자릿수 만큼
        for p in permutations(numbers, i):  # permutations 이용해서 서로 다른 n개 중에서 r개를 뽑아 순서를 고려하여 나열한 경우의 수 구함
            num = int(''.join(p))  # 문자열 -> 정수 변환 (앞자리 0 제거됨)
            number_set.add(num)

    # 소수만 필터링
    prime_count = 0
    for num in number_set:
        if is_prime(num):
            prime_count += 1

    return prime_count

# <피드백>
# # ***from itertools import permutations : 순열 만드는 도구
# # 서로 다른 n개 중에서 r개를 뽑아 순서를 고려하여 나열한 경우의 수 구함
# # 즉 주어진 문자열을 가지고 permutaions(numbers, i) 로 그 개수만큼의 조합을 만듦
# 이걸 int(''.join(p)) 통해서 int 로 만들고 별도의 배열에 담으면 모든 숫자가 들어가게 됨
