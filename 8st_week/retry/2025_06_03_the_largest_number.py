# Q. 가장 큰 수

from functools import cmp_to_key

def compare(a, b):
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    else:
        return 0


def solution(numbers):
    arr = list(map(str, numbers))
    arr.sort(key=cmp_to_key(compare))

    return ''.join(arr)


# <피드백>
# 여기서 permutaions 을 쓰면 안된다
# 문제에서 numbers의 길이가 1 이상 100,000 이하라서 너무 많은 순열이 만들어져서 시간 초과된다

# 해당 문제에서는 정수 배열로 오는 것으로 가장 큰 수 만드는 건데
# 모든 경우의 수를 만들어 sort하는 방법도 있겠지만 너무 수가 많아서
# str 로 변환 후 정렬하는 방식으로 가야한다
# 문자열 a + b 와 b + a 로 비교할 수 있다

# from functools import cmp_to_key 는 필수이다
# 사용법은 sort(key=cmp_to_key(함수))

# list(map(str, arr)) 로 정수 배열을 문자열 배열로 바꿀 수 있다

