# 분할 정복의 개념
# 큰 문제를 작은 2개의 문제로 분리하고 각각을 해결한 다음
# 그 결과를 모아서 해결하는 전략
# 이 병합 정렬에서 예를 들어 [5, 4] 배열이 있다면
# [5], [4] 이렇게 두 개의 배열로 나눠서 생각하는 것이다
# 배열의 길이가 길어지더라도 동일한 형태로 반복 될테니까
# 재귀적인 방법을 떠올릴 수 있다

# 재귀적인 방법은 가장 작은 덩어리부터 값을 구하면서 결과를 합치는 것이라 생각하자
# 진행은 1 -> 2 -> 3 -> 4 지만 결과를 만드는 순서는 4 -> 3 -> 2 -> 1 이 된다

array = [5, 3, 2, 1, 6, 8, 7, 4]

# O(NlogN)
# TODO: 이 재귀의 시간복잡도를 계산하는 것을 이해하기 쉽지 않다 강의를 반복적으로 들어보자
def merge_sort(array):
    if len(array) <= 1: # 길이가 1이면 반으로 못 나누니까 종료 조건
        return array
    mid = (0 + len(array)) // 2 # 중간값
    # array[start:stop] start 부터 시작 해서 stop 직전 까지
    left_array = merge_sort(array[:mid]) # 왼쪽 부터 계속 반복
    right_array = merge_sort(array[mid:]) # 오른쪽 부터 계속 반복
    return merge(left_array, right_array)

# O(N)
def merge(array1, array2):
    result = []
    array1_index = 0
    array2_index = 0

    # 길이 값보다 전(마지막 인덱스)인 조건으로 while문 돌리기
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

    # 각각 남아 있는 것이 있다면 넣어 주기
    while array1_index < len(array1):
        result.append(array1[array1_index])
        array1_index += 1
    while array2_index < len(array2):
        result.append(array2[array2_index])
        array2_index += 1

    return result


print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge_sort([-7, -1, 9, 40, 5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge_sort([-1, 2, 3, 5, 40, 10, 78, 100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge_sort([-1, -1, 0, 1, 6, 9, 10]))