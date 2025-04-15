# 병합정렬
array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]

# i1
# [1, 2, 3, 5]
# i2
# [4, 6, 7, 8]
#
# [1, 2, 3, 4, 5 ...]

# 아이디어
# 각 배열의 0번째 부터 비교를 시작해서
# 새로운 배열에 차례대로 넣어준다
# 넣으면 값이 빠져나갔다 생각하고 인덱스를 +1 하면서 진행해주면 된다
# 마지막까지 다 넣게 되면 반대쪽 배열의 값은 진행중인 인덱스 부터 차례대로 넣어주면 된다

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


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge([-7, -1, 9, 40], [5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge([-1,2,3,5,40], [10,78,100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge([-1,-1,0], [1, 6, 9, 10]))