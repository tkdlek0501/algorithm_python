input = [4, 6, 2, 9, 1]

# 삽입 정렬
# 맨 처음 값은 정렬 돼있다고 가정하고 새로운 것이 들어올 때 정렬하는 방법
# [4, 6, 2, 9, 1]

# for i in range(1, 5):
#     for j in range(i):
        # i - j


def insertion_sort(array):
    n = len(array)

    # O(N^2)
    # O(N) -> 이미 모든 값이 정렬 돼있다면 최소 시간 복잡도
    for i in range(1, n): # 첫번째는 제외하고 그 뒤부터 끝까지 범위로 인덱스 생성
        for j in range(i): # 그 인덱스 이하의 범위로 j를 뽑아내서
            if array[i - j] < array[i - j - 1]: # 새로 들어온 맨 끝 값과 그 전 값부터 비교
                array[i - j], array[i - j - 1] = array[i - j - 1], array[i - j]
            else: # 새로 들어온 값이 이미 정렬된 상태면 그 전 값들은 이미 정렬이 전 단계에서 돼있으므로 비교할 필요가 없다
                break

    return array


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",insertion_sort([5,8,4,7,7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",insertion_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",insertion_sort([100,56,-3,32,44]))