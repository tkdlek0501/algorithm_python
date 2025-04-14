input = [4, 6, 2, 9, 1]

# 선택 정렬
# 매번 모든 요소를 탐색하면서 가장 작은 값을 뽑아 맨 앞으로 이동 시키고
# 그 위치는 다음 반복에서 제외한다

def selection_sort(array):
    n = len(array)
    # O(N^2)
    for i in range(n - 1): # 가장 마지막 값은 자동으로 정렬이 되므로 - 1 범위
        min_index = i  # i = 0
        for j in range(n - i): # j = 0..4
            if array[i + j] < array[min_index]:
                min_index = i + j # 최소값이 존재하는 인덱스를 뽑는다
        array[i], array[min_index] = array[min_index], array[i]

    return array


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",selection_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",selection_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",selection_sort([100,56,-3,32,44]))