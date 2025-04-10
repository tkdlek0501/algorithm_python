# Q. 다음과 같이 숫자로 이루어진 배열이 있을 때,
# 2이 존재한다면 True 존재하지 않는다면 False 를 반환하시오.

# [0, 3, 5, 6, 1, 2, 4]

finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

# 아이디어
# 1. 순차적으로 정렬된 배열이 아니다
# 2. 이를 순차적으로 만드는 작업을 먼저 해야 한다?

def is_exist_target_number_binary(target, array):
    array.sort(array,)

    current_index = (len(array) - 1) // 2
    left_index = 0
    right_index = len(array) - 1

    while left_index <= right_index:
        if array[current_index] == target:
            return True
        else:
            if target > array[current_index]:
                left_index = current_index + 1
            else:
                right_index = current_index - 1
        current_index = (left_index + right_index) // 2

    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)