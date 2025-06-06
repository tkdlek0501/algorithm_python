# 한자리 숫자가 적힌 종이 여러개
# 그 조각들을 붙여 소수를 몇 개 만들 수 있는지
# 숫자가 적힌 문자열 numbers
# 소수가 몇 개 인지 return
# numbers 의 길이는 1이상 7이하 문자열
# numbers는 0~9까지 숫자로만 이루어져 있다

# ex. [1, 7]
# [7, 17, 71]
# -> 즉 1, 7 중 1개 혹은 2개를 꺼내서 만들 수 있는 조합 중 소수인 것 찾기

from itertools import permutations


def solution(numbers):
    answer = 0

    def is_prime(target):  # 소수 판별; 1과 자기 자신으로만 나눠져야 한다
        if target <= 1:
            return False
        for i in range(2, int(target ** 0.5) + 1):
            if target % i == 0:
                return False
        return True

    number_set = set()
    for n in range(1, len(numbers) + 1):  # numbers 의 길이 내에서
        for p in permutations(numbers, n):  # numbers 안에서 n개로 만들 수 있는 조합
            number_set.add(int(''.join(p)))

    for num in number_set:
        if is_prime(num):
            answer += 1

    return answer