# Q. 다음과 같이 숫자로 이루어진 배열이 있을 때, 이 배열 내에서 가장 큰 수를 반환하시오.
# [3, 5, 6, 1, 2, 4]

# [코드스니펫] 최댓값 찾기 문제
# def find_max_num(array):
#     # 이 부분을 채워보세요!

# 내 아이디어 정리
# 1. 배열이 주어졌으니까 for 문을 사용해서 순환해서 찾아야 함
# 2. 최댓값을 찾아야 하니까 순환마다 비교해서 큰 수를 임의의 변수로 대입해야 함
# 3. 모든 순환이 끝나면 그 변수 값이 곧 최댓값이 됨

# 내 풀이
# 피드백 -> 파이썬 문법에 아직 적응 하지 못해서 if 문에 소괄호 작성 실수, 콜론 사용에 어색함
def find_max_num(array):
    max = array[0]
    for element in array :
        if (max < element) :
            max = element
    return max

print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))

# 정답
def find_max_num(array):
    max_num = array[0]
    for num in array:
        if num > max_num:
            max_num = num
    return max_num

print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))