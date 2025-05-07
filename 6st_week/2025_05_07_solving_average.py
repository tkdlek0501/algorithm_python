# Q. 평균 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12944

# 문제 설명
# 정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.
#
# 제한사항
# arr은 길이 1 이상, 100 이하인 배열입니다.
# arr의 원소는 -10,000 이상 10,000 이하인 정수입니다.
# 입출력 예
# arr	return
# [1,2,3,4]	2.5
# [5,5]	5

# <문제분석>
# 배열 arr 안의 정수들의 평균값을 return
# 1 <= arr 길이 <= 100
# arr 내 원소는 -10,000 <= n <= 10,000 정수

# <구현>
# 배열 내 모든 수의 합 / 모든 수의 개수

def solution(arr):
    sum = 0
    for n in arr:
        sum += n

    return sum / len(arr)

# 더 좋은 방법
def average(list):
    return sum(list) / len(list)
    # 배열의 모든 수의 합을 sum(배열) 로 그냥 구할 수 있다..

# 아래는 테스트로 출력해 보기 위한 코드입니다.
list = [5,3,4]
print("평균값 : {}".format(average(list)));