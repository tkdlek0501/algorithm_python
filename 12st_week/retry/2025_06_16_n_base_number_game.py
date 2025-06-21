# Q. n 진수 게임

# <문제분석>
# 여러 사람이 둥글게 앉아서 숫자를 하나씩 차례대로 말하는 게임
# 규칙
# 1. 0부터 시작해서 차례대로 말한다
# 2. 10 이상 숫자부터는 한 자리씩 끊어서 말한다
# -> 열한 번째 사람의 10의 첫 자리인 1, 열두 번째 사람은 둘째 자리인 0을 말한다

# 이진수로 이 게임을 진행하기도 한다
# 0, 1, 1, 0, 1, 1, 1, ...

# 이진법에서 십육진법까지 모든 진법으로 게임
# 튜브가 말해야 하는 숫자 t개를 공백 없이 차례대로 나타낸 문자열
# *단 10~15는 A~F로 출력한다

# <풀이>
# 십진수를 기반으로 구해야 하는 것
# 진법 변환이 필요하다

def solution(n, t, m, p): # 진법, 미리 구할 숫자의 개수, 게임 인원, 순서
    sequence = ""
    number = 0

    while len(sequence) < t * m:
        sequence += convert(number, n)
        number += 1

    answer = ""
    for i in range(t):
        answer += sequence[(i * m) + (p - 1)]

    return answer

def convert(num, base):
    digits = "0123456789ABCDEF"
    if num == 0:
        return "0"
    result = ""
    while num > 0:
        result = digits[num % base] + result
        num //= base
    return result

# <피드백>
# 진법 변환 함수에 익숙해지자
# 미리 sequence 를 만들어 놓고 거기서 내 순서의 값만 뽑아오면 되는 구현 문제
# 내 순서 = 해당 라운드에서 p 번째 = (i * m) + (p - 1)

