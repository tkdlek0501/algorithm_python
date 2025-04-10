finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_sequential(target, array):
    for number in array:
        if target == number:
            return True

    return False


result = is_existing_target_number_sequential(finding_target, finding_numbers)
print(result)  # True

# Tip. 숫자 내림 하는 방법
# >>> print((4 + 5) / 2)
# 4.5
# >>> print((4 + 5) // 2)
# 4   # 소숫점 이하 자리를 버리게 된다