# Q. 약수의 개수와 덧셈
# 문제 설명
# 두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.
#
# 제한사항
# 1 ≤ left ≤ right ≤ 1,000
# 입출력 예
# left	right	result
# 13	17	43
# 24	27	52
# 입출력 예 설명
# 입출력 예 #1
#
# 다음 표는 13부터 17까지의 수들의 약수를 모두 나타낸 것입니다.
# 수	약수	약수의 개수
# 13	1, 13	2
# 14	1, 2, 7, 14	4
# 15	1, 3, 5, 15	4
# 16	1, 2, 4, 8, 16	5
# 17	1, 17	2
# 따라서, 13 + 14 + 15 - 16 + 17 = 43을 return 해야 합니다.
# 입출력 예 #2
#
# 다음 표는 24부터 27까지의 수들의 약수를 모두 나타낸 것입니다.
# 수	약수	약수의 개수
# 24	1, 2, 3, 4, 6, 8, 12, 24	8
# 25	1, 5, 25	3
# 26	1, 2, 13, 26	4
# 27	1, 3, 9, 27	4
# 따라서, 24 - 25 + 26 + 27 = 52를 return 해야 합니다.

# <문제분석>
# 두 정수 left, right
# left 부터 right 까지 모든 수 중
# 약수의 개수가 짝수인 수는 더하고
# 약수의 개수가 홀수인 수는 뺀 수를 return

# <풀이>
# left 부터 right 까지
# 약수의 개수 구하기

def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        count = 0  # 약수의 개수
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        if count % 2 == 0:  # 짝수
            answer += num
        else:
            answer -= num

    return answer

# <피드백>
# 제곱수가 약수가 되면 그 약수의 개수가 홀수 이고
# 그렇지 않으면 짝수이다라는 것을 알면
# 굳이 약수의 개수를 직접 구하지 않아도 홀짝을 알 수 있어 아래와 같이 구할 수 있다
def solution1(left, right):
    answer = 0
    for i in range(left,right + 1):
        if int(i ** 0.5) == i ** 0.5:
            answer -= i
        else:
            answer += i
    return answer
