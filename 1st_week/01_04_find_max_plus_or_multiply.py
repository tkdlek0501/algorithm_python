# Q. 다음과 같이 0 혹은 양의 정수로만 이루어진 배열이 있을 때,
# 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며
# 숫자 사이에 '✕' 혹은 '+' 연산자를 넣어
# 결과적으로 가장 큰 수를 구하는 프로그램을 작성하시오.
# 단, '+' 보다 '✕' 를 먼저 계산하는 일반적인 방식과는 달리,
# 모든 연산은 왼쪽에서 순서대로 이루어진다.

# 아이디어
# 1. 왼쪽 값과 오른쪽 값의 연산에서 각각 0이나 1이라면 더하는 게 낫고 아니면 곱하는 게 낫다
# 2. 왼쪽 값과 오른쪽 값의 합으로 if문을 만들어 처리
# 3. ex) 0 + 1 vs. 0 * 1 / 0 * 8 vs. 0 + 8 ...

def find_max_plus_or_multiply(array):
    # 이 부분을 채워보세요!
    result = 0
    for number in array: # O(N)
        if number <= 1 or result <= 1:
            result += number
        else:
            result *= number
    return result



result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))
