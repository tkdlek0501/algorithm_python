# Q. 행렬의 덧셈
# 문제 설명
# 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.
#
# 제한 조건
# 행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.
# 입출력 예
# arr1	arr2	return
# [[1,2],[2,3]]	[[3,4],[5,6]]	[[4,6],[7,9]]
# [[1],[2]]	[[3],[4]]	[[4],[6]]

def solution(arr1, arr2):
    answer = [[0] * len(arr1[0]) for _ in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer

# <피드백>
# list에 추가가 아닌 특정 위치에 값을 넣으려면
# 초기화가 반드시 필요하다

# 아래 코드 처럼 초기화와 동시에 요소를 넣을 수 있다
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a,b)] for a, b in zip(A,B)]
    return answer