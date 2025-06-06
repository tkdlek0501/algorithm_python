# TODO: 다시 풀어보기 - 소수 찾기
# Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오.
# 소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.

# 20이 입력된다면, 아래와 같이 반환해야 합니다!
# [2, 3, 5, 7, 11, 13, 17, 19]

# 아이디어

input = 20

# 1. 소수는 자기 자신과 1 외에는 아무 것도 나눌 수 없다.
# def find_prime_list_under_number(number):
#     prime_list = []
#
#     # 2~number 까지 찾아서 이것들이 소수이면 prime_list 넣는다.
#     for n in range(2, number + 1): # 2 ~ n 까지의 숫자들이 n에 들어가는 것을 반복한다
#         # 이것들이 소수인가?
#         print(prime_list)
#         for i in range(2, n): # 2부터 n-1 까지 i 에 들어가는 것을 반복 (1과 자기 자신 제외)
#             if n % i == 0: # 나누어 떨어지면 소수가 아니다
#                 break
#         else:
#             prime_list.append(n)
#     return prime_list
# 위 방식은 효율적이지 않다.
# n이 19라고 가정한다면 i는 2 ~ 18 이 되는데
# 2와 3으로 나누어 떨어지지 않으면 4, 6 등은 당연히 안 나누어 떨어질텐데 for문을 돌아야 한다
# 즉 소수로 나누어 떨어지는 지만 확인하면 된다

# def find_prime_list_under_number(number):
#     prime_list = []
#
#     # 2~number 까지 찾아서 이것들이 소수이면 prime_list 넣는다.
#     for n in range(2, number + 1): # 2 ~ n 까지의 숫자들이 n에 들어가는 것을 반복한다
#         # 이것들이 소수인가?
#         for i in prime_list: # 2부터 n-1 까지 i 에 들어가는 것을 반복 (1과 자기 자신 제외)
#             if n % i == 0: # 나누어 떨어지면 소수가 아니다
#                 break
#         else:
#             prime_list.append(n)
#     return prime_list
# 여기서 더 개선할 수 있다.
# N의 제곱근 보다 크지 않은 어떤 소수로도 나누어 떨어지지 않는다 라는 소수의 개념을 사용하면 된다.
# i * i <= n 까지 검사하면 된다

def find_prime_list_under_number(number):
    prime_list = []

    # 2~number 까지 찾아서 이것들이 소수이면 prime_list 넣는다.
    for n in range(2, number + 1): # 2 ~ n 까지의 숫자들이 n에 들어가는 것을 반복한다
        # 이것들이 소수인가?
        for i in prime_list: # 소수로만 검사
            if i * i <= n and n % i == 0: # i * i <= n 이라는 소수의 개념 + 나누어 떨어지면 소수가 아니다
                break # 소수가 아니다
        else:
            prime_list.append(n)
    return prime_list

result = find_prime_list_under_number(input)
print(result)

# 소수 문제 풀이의 핵심 개념 정리
# 어떤 수 n이 소수가 아니라면, 반드시 더 작은 소수의 곱으로 표현됨(=그 소수로 나눠진다)
# 1. 즉 어떤 수가 소수인지 판별하려면 소수로만 검사하면 된다.
# 2. 나눠보는 소수는 i * i <= n 까지만 검사하면 된다
# 왜냐면 n 이 합성수라면 그 약수 중 하나는 반드시 n의 제곱근 이하이기 때문

# 파이썬의 문법 for-else
# for x in [1,2,3,4]:
#     print(x)
#     if x == 4:
#         break
# else: # for 문이 정상적으로 모두 완료 되었다면 실행
#     print("완료되었습니다.")