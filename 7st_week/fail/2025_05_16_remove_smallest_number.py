# Q. 제일 작은 수 제거하기
# 문제 설명
# 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요. 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.
#
# 제한 조건
# arr은 길이 1 이상인 배열입니다.
# 인덱스 i, j에 대해 i ≠ j이면 arr[i] ≠ arr[j] 입니다.
# 입출력 예
# arr	return
# [4,3,2,1]	[4,3,2]
# [10]	[-1]


# <문제분석>
# 정수 배열 arr
# 가장 작은 수를 제거한 배열을 return
# *단, return 하려는 배열이 빈 배열이면 -1을 채워 return

# <풀이>
# 가장 작은 수를 제거해야 한다
# 순서는 유지?
# 제한 조건에 같은 값이 없다는 것을 알려주고 있다

def solution(arr):
    if len(arr) == 1:
        return [-1]
    arr_copy = arr.copy()
    arr_copy.sort(reverse=True)
    deleted = arr_copy.pop()

    answer = []
    for i in range(len(arr)):
        if arr[i] != deleted:
            answer.append(arr[i])
    return answer

# <피드백>
# 주의! array 등 변수를 copy 할 때는
# arr_copy = arr 로 깊은 복사를 하면 안된다
# arr_copy = arr.copy() 를 통해 얕은 복사를 해야 같은 객체를 참조하지 않는다

# arr 에는 arr.remove() 함수도 있고,
# min(arr) 로 가장 작은 수를 찾아올 수도 있다
def rm_small(mylist):
    if len(mylist) == 1:
        return [-1]
    mylist.remove(min(mylist))
    return mylist

