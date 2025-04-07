# Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오.
# 소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.

# 20이 입력된다면, 아래와 같이 반환해야 합니다!
# [2, 3, 5, 7, 11, 13, 17, 19]

# 아이디어
# 1. 1과 자기 자신으로 검사할 필요는 없다
# 2. i * i <= n 일 때만 i로 나누는 검사가 의미 있다 나눠지면 소수가 아니다 / 나눠지지 않으면 소수이다
# 3. 소수로만 검사하면 된다

input = 20

def find_prime_list_under_number(number):
    prime_list = []

    for n in range(2, number + 1): # 1은 제외하고 2부터 자기 자신 포함
        for i in prime_list: # 값을 꺼내서 비교
            if i * i <= n and n % i == 0:
                break
        else:
            prime_list.append(n)

    return prime_list

result = find_prime_list_under_number(input)
print(result)