# 문제 설명
# 정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.
#
# 제한 조건
# num은 int 범위의 정수입니다.
# 0은 짝수입니다.
# 입출력 예
# num	return
# 3	"Odd"
# 4	"Even"


# <문제분석>
# 정수 num 이 짝수이면 Even
# 홀수이면 Odd를 반환
# num은 int 범위의 정수이고
# 0은 짝수이다

# <구현>
# %2 로 나누어서 나머지 없이 나누어 떨어지면 "Even"
# 나머지가 0 을 초과하면 "Odd"

num = 3 # "Odd"
# num = 4 "Even"

def solution(num):
    answer = ''

    if num % 2 > 0:
        answer = "Odd"
    else:
        answer = "Even"

    return answer

# 더 좋은 방법
def evenOrOdd(num):
    if num % 2: # 나머지가 있다면 True or False
        return "Odd"

    return "Even"

print(solution(num))