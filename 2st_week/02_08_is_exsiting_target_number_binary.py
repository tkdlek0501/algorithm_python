finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# 아이디어
# 1. 중간을 먼저 구해야 한다.
# 2. 중간값보다 큰지 안큰지 비교 후 크다면 그 이상의 인덱스 부터, 작다면 그 미만의 인덱스부터
# 또 중간을 구해서 위 과정을 반복한다
# 3. 같다면 return 한다

# 내 풀이
# def is_existing_target_number_binary(target, array):
#     center_index = (len(array) - 1) // 2
#
#     num = 0
#     left_index = 0
#     right_index = len(array) - 1
#     while num != target:
#         num = array[center_index]
#         if num == target:
#             print("index : ", center_index, "num : ", num)
#             return True
#         else:
#             if target > num:
#                 left_index = center_index + 1
#                 center_index = (left_index + right_index) // 2
#             else:
#                 right_index = center_index - 1
#                 center_index = (left_index + right_index) // 2
#
#     return False

# 시간 복잡도 계산
# array 길이가 N
# 1 ... N -> 1 ... N/2 -> 1 ... N/4 -> 1 ... N/8 ~> 1 ... N/2^k
# N/2^k = 1 이 되려면
# N = 2^k
# log_2(N) = k
# O(log(N)) 만큼의 시간 복잡도
# 계산 없이 쉽게 생각 하려면 횟수가 감소할 때마다 2차 함수 형태로 탐색 범위가 감소하는 경향을 보이면
# O(log(N)) 이다라고 생각하면 된다

def is_existing_target_number_binary(target, array):
    find_count = 0
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2

    while current_min <= current_max:
        find_count += 1
        if array[current_guess] == target:
            print(find_count)
            return True
        else:
            if target > array[current_guess]:
                current_min = current_guess + 1
            else:
                current_max = current_guess - 1
        current_guess = (current_min + current_max) // 2

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)


# Tip. 숫자 내림 하는 방법
# >>> print((4 + 5) / 2)
# 4.5
# >>> print((4 + 5) // 2)
# 4   # 소숫점 이하 자리를 버리게 된다