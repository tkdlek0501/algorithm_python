# Q. 문자열 내림차순으로 배치하기

# 문제 설명
# 문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
# s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.
#
# 제한 사항
# str은 길이 1 이상인 문자열입니다.
# 입출력 예
# s	return
# "Zbcdefg"	"gfedcbZ"

# <문제분석>
# 문자열 s에 나타나는 문자를 큰 것부터 작은 순으로 정렬
# s는 영문 대소문자로만 구성돼있고 대문자는 소문자보다 작은 것으로 간주
# s은 길이 1 이상

def solution(s):
    answer = ''
    arr = []
    for chr in s:
        arr.append(chr)
    arr.sort(reverse=True)
    for i in arr:
        answer += i
    return answer

# <피드백>
# for문을 없애려면 join 을 쓰면 된다
# array를 str로 바꾸기 위해서 ''.join(arr) 쓸 수 있다
# 여기서 주의점은 sorted(str) 을 쓰면 자동으로 문자열이 array로 형변환 된다는 점(굳이 변환 과정 필요 없음)

def solution1(s):
    return ''.join(sorted(s, reverse=True))