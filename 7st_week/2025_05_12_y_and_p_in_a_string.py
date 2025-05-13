# 문제 설명
# 대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.
#
# 예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.
#
# 제한사항
# 문자열 s의 길이 : 50 이하의 자연수
# 문자열 s는 알파벳으로만 이루어져 있습니다.
# 입출력 예
# s	answer
# "pPoooyY"	true
# "Pyy"	false
# 입출력 예 설명
# 입출력 예 #1
# 'p'의 개수 2개, 'y'의 개수 2개로 같으므로 true를 return 합니다.
#
# 입출력 예 #2
# 'p'의 개수 1개, 'y'의 개수 2개로 다르므로 false를 return 합니다.

# <문제분석>
# 대소문자가 섞여있는 문자열 s가 주어짐
# s 에 'p'의 개수와 'y'의 개수를 비교해 같으면 True 다르면 False 출력
# -> 설명에서 대소문자 구분하지 않음
# 모두 하나도 없으면 True return
# 문자열 s 길이 50 이하
# 문자열 s는 알파벳으로만 이루어져 있다

# <풀이>

def solution(s):
    answer = True

    y_count = 0
    p_count = 0

    for i in range(len(s)):
        char = s[i]
        if char == 'y' or char == 'Y':
            y_count += 1
            continue
        if char == 'p' or char == 'P':
            p_count += 1

    return y_count == p_count


# <피드백>
# 더 좋은 방법으로
# lower() 로 소문자 변환과
# count('p') 라는 집계함수 를 사용한 방법이 있다

def numPY(s):
    return s.lower().count('p') == s.lower().count('y')