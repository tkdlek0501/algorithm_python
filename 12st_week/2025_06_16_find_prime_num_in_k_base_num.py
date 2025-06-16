# Q. k진수에서 소수 개수 구하기

# <문제분석>
# 양의 정수 n 주어지면
# k 진수로 바꿨을 때
# 변환된 수 안에 아래 조건에 맞는 소수가 몇 개인지 알아내야 한다

# 0P0 처럼 소수 양쪽에 0이 있는 경우
# P0 처럼 소수 오른쪽에만 0이 있고 왼쪽에는 아무것도 없는 경우
# 0P 처럼 소수 왼쪽에만 0이 있고 오른쪽에는 아무것도 없는 경우
# P 처럼 소수 양쪽에 아무것도 없는 경우
# *단 P는 각 자릿수에 0을 포함하지 않는 소수
# ex. 101은 P가 될 수 없다

# ex. 437674 를 3진수로 바꾸면
# 211/0/2/01010/11
# 조건에 맞는 소수는 왼쪽 부터 211, 2, 11 : 3개
# 211, 2, 11은 10진법 기준으로 소수여야 한다

# <풀이>
# 1. 정수 n을 k 진수로 바꾼다
# 2. 변환된 수를 가지고 잘라내서 판단해야 한다
# 3. 0으로 문자열을 나눠서 판단한다?

def solution(n, k):  # 정수, k진법
    answer = 0

    def convert(num, l):
        digits = "0123456789ABCDEF"
        result = ""
        if num == 0:
            result = "0"
        else:
            while num > 0:
                result = digits[num % l] + result
                num //= l
        return result

    def is_prime(s):
        num = 0
        if s == '':
            return False
        else:
            num = int(s)
        if num == 1:
            return False
        else:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
        return True

    changed_num = convert(n, k)
    arr = changed_num.split('0')

    for a in arr:
        if is_prime(a):
            answer += 1

    return answer

# <피드백>
# 진법 변환 함수와
# 소수 판별 함수
# 그리고
# 211/0/2/01010/11 이 규칙을 가지고 풀면 된다

# n을 k진법으로 나타낸 문자열 반환
def conv(n, k):
    s = ''
    while n:
        s += str(n%k)
        n //= k
    return s[::-1]

# n이 소수인지 판정
def isprime(n):
    if n <= 1: return False
    i = 2
    while i*i <= n:
        if n%i == 0: return False
        i += 1
    return True

def solution1(n, k):
    s = conv(n,k)
    cnt = 0
    for num in s.split('0'):
        if not num: continue # 빈 문자열에 대한 예외처리
        if isprime(int(num)): cnt += 1
    return cnt