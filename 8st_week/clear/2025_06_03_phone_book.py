# Q. 전화번호 목록

# 전화번호 중 한 번호가 다른 번호의 접두어인 경우가 있는지 확인
# ex.
# 119
# 07 674 223
# 11 9552 4421 -> 119가 접두어

# 전화번호 배열 phone_book 입력
# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false / 없으면 true

# <풀이>
# 배열안의 요소들을 정렬하면 비슷한 것 끼리 모임
# 이전 것과 다음 것만 비교해서 반환
# 비교는 어떻게? 그냥 in 하면 되나? x startswith 쓰기

def solution(phone_book):
    phone_book.sort()

    for i in range(0, len(phone_book) - 1):
        a, b = phone_book[i], phone_book[i + 1]
        if b.startswith(a):
            return False

    return True