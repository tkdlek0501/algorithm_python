# Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오.
# 소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.

# 20이 입력된다면, 아래와 같이 반환해야 합니다!
# [2, 3, 5, 7, 11, 13, 17, 19]

# 아이디어
# 1. 정수를 입력 받고 그 이하의 값 중 소수면 array 에 넣어둬야 한다
# 2. 소수인지를 검사하려면? 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없어야 하고 1보다 커야 한다

input = 20

def find_prime_list_under_number(number):

    return []


result = find_prime_list_under_number(input)
print(result)