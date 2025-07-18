# Q. 최솟값 만들기

def solution(A, B):  # 자연수 배열
    answer = 0
    A.sort()
    B.sort(reverse=True)

    for a, b in zip(A, B):
        answer += (a * b)

    return answer

# 가장 작은 값 * 가장 큰 값 이 가장 작은 합을 만드는 것임을 알면 쉽다
