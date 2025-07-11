# Q. 파일명 정렬

# <문제분석>
# 파일명 정렬
# 이름 순 정렬시 ver-10.zip 이 ver-9.zip 보다 먼저 표시됨
# 파일명을 100글자 이내, 영문 대소문자, 숫자, 공백, 마침표, 빼기 부호
# 영문자로 시작하며 숫자를 하나 이상 포함하고 있다

# 파일명은 세 부분으로 구성된다
# HEAD : 숫자가 아닌 문자로 이루어져 있고, 최소 한 글자 이상
# NUMBER : 한 글자에서 최대 다섯 글자 사이의 연속된 숫자, 앞에 0이 올 수 있다
# TAIL : 나머지 부분, 숫자가 있을 수도 있고 아무 글자도 없을 수 있다

# 파일명은 우선 HEAD 부분 기준으로 사전 순 정렬
# 대소문자 구분은 하지 않음

# HEAD 부분이 같다면, NUMBER 숫자 순으로 정렬

# HEAD, NUMBER 같으면 원래 주어진 순서를 유지

# <풀이>
# 1. HEAD, NUMBER 로 나눈다 (TAIL 필요 없음)
# -> 원래 배열의 index : (HEAD, NUMBER)
# 2. HEAD 기준으로 정렬
# for 문 돌면서 HEAD 같으면 NUMBER 기준으로 정렬 -> 앞뒤 체크?

import re
def split_file(file):
    match = re.match(r'([^\d]+)(\d{1,5})', file)
    head, number = match.group(1), match.group(2)
    return head, number

def solution(files):
    return sorted(files, key=lambda f: (split_file(f)[0].lower(), int(split_file(f)[1])))

# <피드백>
# 숫자, 문자 구분 등 여러 요건 충족하려면 정규식이 베스트이다
# import re
# match = re.match(정규식, 원문자열)
# match.group(1), match.group(2), ...
# return head, number -> split_file(file)[0] / [1] 로 return 받을 수 있다

# ([^\d]+) : 숫자가 아닌(문자) 것 캡처
# (\d{1,5}) : 숫자인 것 1개부터 5개까지 캡처
# file[match.end():] 으로 나머지 TAIL 부분도 가지고 올 수 있음
# 숫자 추출	\d+
# 알파벳 추출	[a-zA-Z]+
# 공백 추출	\s+
# 숫자 아닌 것	[^0-9]
# 반복	+, {1,5}
# r'...' 쓰는 이유 -> \를 두 번 쓸 필요 없게 해줌	\\d → \d 등 쉽게 쓸 수 있게 해줌


# sorted(iterable, key=정렬기준함수)
# files, key=lamda f: (함수(f), 함수(f))
# 함수의 결과로 받아온 튜플로 정렬 기준을 만들어 줄 수 있다

# 정규식으로 못풀겠다 하면 아래 방법
def solution1(files):
    answer = []

    dict = {}
    for i in range(len(files)):
        file = files[i]
        idx = 0
        head = ""
        # head 만들기
        for ch in file:  # 글자들을 돌면서
            if ch.isdigit():  # 숫자이면
                break
            else:
                if ch.isalpha():  # 영문자이면
                    head += ch.upper()
                else:
                    head += ch
                idx += 1

        # number 만들기
        number = ""
        max_number = 5
        for j in range(idx, len(file)):
            if not file[j].isdigit():
                break
            if len(number) >= max_number:
                break
            number += file[j]

        dict[i] = (head, int(number))

    sorted_items = sorted(
        dict.items(),
        key=lambda item: (item[1][0].lower(), item[1][1], item[0]))

    for s in sorted_items:
        answer.append(files[s[0]])

    return answer

# <피드백>
# sorted(dict.items()) # 를 통해 (key, value) 가져올 수 있고
# key=lamda item: 하면 이게 하나의 (key, value)
# (item[0] 이 key 이고 item[1]이 value 가 된다)
# 마지막에 item[0] (key 값 = 기존 인덱스) 을 넣음으로써 안정 정렬 도 해줘야 기존 정렬 유지 케이스까지 만족할 수 있다
