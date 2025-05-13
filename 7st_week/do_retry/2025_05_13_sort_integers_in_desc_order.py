# Q. 정수 내림차순으로 배치하기
# 문제 설명
# 함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.
#
# 제한 조건
# n은 1이상 8000000000 이하인 자연수입니다.
# 입출력 예
# n	return
# 118372	873211

def solution(n):
    answer = 0

    n_copy = n

    arr = []
    while n_copy != 0:
        arr.append(n_copy % 10)
        n_copy //= 10
    arr.sort(reverse=True)

    for i in range(len(arr)):
        answer += arr[-(i + 1)] * (10 ** i)

    return answer

# <피드백>
# 더 좋은 방법으로 string을 리스트로 변환하는 함수를 사용하면 변환이 쉽다
# str(n) 으로 먼저 정수를 문자열로 바꾸고
# list(str) 로 문자열을 배열로 바꿀 수 있다
# 이후 array.sort(reverse = True) 이용해서 내림차순 해주고
# 다시 string을 int 로 바꾸기 위해 int() 를 써야하는데
# 그 전에 join(array) 를 써서 다시 array를 string으로 만든 뒤 int로 변환

def solution1(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))