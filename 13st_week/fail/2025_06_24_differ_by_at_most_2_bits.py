# Q. 2개 이하로 다른 비트

# <문제분석>
# 양의 정수 x 에 대한 함수 f(x)
# x 보다 크고 x와 비트가 1~2개 다른 수들 중에서 제일 작은 수

# ex.
# f(2) = 3
# 2 -> 000...0010 / 0개
# 3 -> 000...0011 / 1개

# f(7) = 11
# 7 -> 0111
# 8 -> 1000 / 4
# 9 -> 1001 / 3
# 10 -> 1010 / 3
# 11 -> 1011 / 2개

# numbers 길이 <= 100,000
# numbers의 수 <= 10^15

# <풀이>
# bin 값을 가져와서 비교해야 한다?
# 다른 수가 나올 때 까지 while 문?

# def solution(numbers):  # 정수들이 담긴 배열
#     answer = []
#
#     for num in numbers:
#         n = bin(num)[2:]
#         if len(n) < 4:
#             for _ in range(4 - len(n)):
#                 n = '0' + n
#         m = num
#         while True:
#             m += 1
#             m_num = bin(m)[2:]
#             if len(m_num) < 4:
#                 for _ in range(4 - len(m_num)):
#                     m_num = '0' + m_num
#             count = 0
#             for i in range(len(n)):
#                 if n[i] != m_num[i]:
#                     count += 1
#             if count <= 2:
#                 answer.append(m)
#                 break
#
#     return answer

def solution(numbers):
    answer = []
    for number in numbers:
        if number % 2 == 0: # 짝수이면
            answer.append(number + 1) # 자기보다 +1 큰 수가 비트 1개 차이
        else: # 홀수이면
            # 0b...0111 → 0b...1011 같은 패턴으로
            answer.append(number + 1 + ((number ^ (number + 1)) >> 2))
    return answer

# <피드백>
# 짝수: 가장 마지막 비트가 0이므로 +1만 해도 1비트만 달라짐 → f(x) = x + 1
#
# 홀수: 비트 중 가장 낮은 0의 위치를 찾아 그 비트만 1로 바꾸고
# 그 오른쪽 비트를 0으로 바꾸면 2비트만 차이.
# -> number + 1 로 가장 오른쪽 0을 1로 바꾸고,
# -> number ^ (number + 1) 로 바뀐 비트를 파악
# -> >>2 로 가장 작은 2개의 비트 변화는 무시하고 나머지 위치 계산
# * 홀수 일 때 number + 1 + ((number ^ (number + 1)) >> 2) 이 공식 모르면 거의 못 푸는 문제
