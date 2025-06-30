# Q. 가장 큰 수
# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.
#
# 제한 사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
# 입출력 예
# numbers	return
# [6, 10, 2]	"6210"
# [3, 30, 34, 5, 9]	"9534330"

from functools import cmp_to_key
def compare(a, b): # 문자열 형태의 숫자값을 받아서
    if a + b > b + a: # a + b가 더 크므로
        return -1 # a가 b보다 먼저오게
    elif a + b < b + a:
        return 1
    else:
        return 0

def solution(numbers):
    str_nums = list(map(str, numbers))
    str_nums.sort(key=cmp_to_key(compare))

    if str_nums[0] == '0':
        return '0'

    return ''.join(str_nums)

# <피드백>
# from functools import cmp_to_key 는 기억나고
# sort(key = cmp_to_key(compare) 도 쓸 줄 아는데
# 문자열 정렬에서 a + b > b + a: return -1
# 이렇게 두 문자의 합으로 비교해야 한다는 사실을 잊으면 안된다
# list(map(str, numbers)) 문법도 기억해두자
#     if str_nums[0] == '0':
#         return '0'
# 이 부분도 예외적인 처리가 필요하다