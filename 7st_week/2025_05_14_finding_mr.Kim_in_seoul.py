# Q. 서울에서 김서방 찾기
# 문제 설명
# String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요. seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.
#
# 제한 사항
# seoul은 길이 1 이상, 1000 이하인 배열입니다.
# seoul의 원소는 길이 1 이상, 20 이하인 문자열입니다.
# "Kim"은 반드시 seoul 안에 포함되어 있습니다.
# 입출력 예
# seoul	return
# ["Jane", "Kim"]	"김서방은 1에 있다"

def solution(seoul):
    for i in range(len(seoul)):
        if "Kim" == seoul[i]:
            return "김서방은 " + str(i) + "에 있다"

# <피드백>
# array.index(요소의 값) 을 이용하여
# 요소의 인덱스를 확인할 수 있다
# 추가로 string 에 포맷팅을
# "{}".format(str) 로 할 수 있다

def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))