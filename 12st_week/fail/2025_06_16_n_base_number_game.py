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
# 우선 주어진 10 진법으로 된 숫자를 주어진 n진법으로 변환해야 한다
# convert 함수는 숫자와 변환할 진법을 매개변수로 받아서
# 16진법까지 표현하는 "0123456789ABCDEF" 기반으로 변환하는 함수이다
# num이 0일 때를 제외하고는 모두 변환이 필요하다
# 변환할 진법의 수로 10진법의 수를 구할 수 있다
# while num > 0:
# result = digits[num % base] + result
# num //= base

# 주어진 미리구 할 숫자 개수 * 게임 인원만큼 의 수를 만들어야 하므로 while 문 조건에 쓰고
# sequence에 담아 줄 것이며 convert(number, n) 으로 구현해 줄 것이다
# 미리 구할 숫자의 개수만큼 for문 돌아서 answer에 담아줘야 한다
# sequence에 담아놨던 것들 중 (i * m) + (p - 1) 로 자신의 순서의 것들만
# 뽑아서 담아준다

