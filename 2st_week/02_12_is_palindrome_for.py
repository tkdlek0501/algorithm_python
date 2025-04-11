# Q. 다음과 같이 문자열이 입력되었을 때,
# 회문이라면 True 아니라면 False 를 반환하시오.
from os.path import split

# "abcba" # True

# 아이디어
# 맨 처음 글자와 맨 마지막 글자부터 비교하며
# 범위를 좁히면서 같은지 검사해서 같으면 True를 반환한다
# 매 반복 마다 같은 로직이 수행되니 재귀를 쓴다

input = "abcba"

# 1. abcba -> aa 제거
# 2. bcb -> bb 제거
# 3. c -> 한자리만 남았으니 True
# 만약 짝수 개의 길이라도 <= 1 조건을 쓰면 된다
def is_palindrome(string):
    if string[0] != string[-1]:
        return False
    if len(string) <= 1:
        return True

    # 파이썬에서 문자열을 자르는 방법 string[n, m]
    # n 번 인덱스 부터 m번의 앞 인덱스 까지 잘라온다
    return is_palindrome(string[1:-1]) # 여기서 -1은 맨뒤 인덱스의 앞에 까지를 의미


print(is_palindrome(input))