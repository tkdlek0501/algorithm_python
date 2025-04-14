#TODO: 다시 풀어보기! minus or plus 해서 원하는 값이 나오는 경우의 수를 구하기
# Q. 음이 아닌 정수들로 이루어진 배열이 있다.
# 이 수를 적절히 더하거나 빼서 특정한 숫자를 만들려고 한다.
# 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들기 위해서는
# 다섯 방법을 쓸 수 있다.
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
#
# 사용할 수 있는 숫자가 담긴 배열 numbers,
# 타겟 넘버 target_number이 매개변수로 주어질 때
# 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 반환하시오.

# 아이디어
# 이렇게 규칙성이 보이지 않는 문제의 경우에는 당황하지 말고 간단한 예시를 만들어야 한다
# 일관적인 수학적 규칙이 없다면 모든 경우의 수를 찾아야 한다
# 만약 numbers 가 [2, 3, 1], target_number 는 0 로 왔다고 하면
# +2 +3 +1
# +2 +3 -1

# N의 길이의 배열에서 더하거나 뺀 모든 경우의 수는
# N -1 의 길이의 배열에서 마지막 원소를 더하거나 뺀 경우의 수를 추가하면 된다
# [2, 3]을 배치하는 경우의 수에서
# 맨 마지막 원소인 1을 더하냐 빼냐에 따라서 [2,3,1] 의 경우의 수를 구할 수 있다

# +2 -3 +1
# +2 -3 -1
# -2 +3 +1
# -2 +3 -1
# -2 -3 +1
# -2 -3 -1

# 쉽게 생각 해보면 더하냐 빼냐 2가지를 이용해서 모든 경우의 수를 만들어야 하니까
# 매번 더하고 빼는 것을 반복하기 위한 재귀를 만들면서 합을 저장하고 있으면
# target number에 해당하는 합의 개수를 구할 수 있다

numbers = [1, 1, 1, 1, 1]
target_number = 3

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    all_aways = []

    # 값을 더하냐 빼냐에 따라 계산하는 메서드 -> 2개의 재귀를 통해 더하거나 빼는 모든 경우의 수를 만든다
    def get_all_ways_by_doing_plus_or_minus(array, current_index, current_sum):
        if current_index == len(array):
            all_aways.append(current_sum)
            return current_sum

        get_all_ways_by_doing_plus_or_minus(array, current_index + 1, current_sum + array[current_index])
        get_all_ways_by_doing_plus_or_minus(array, current_index + 1, current_sum - array[current_index])

    get_all_ways_by_doing_plus_or_minus(array, 0, 0)

    target_count = 0
    for way in all_aways:
        if target == way:
            target_count += 1
    return target_count

print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!