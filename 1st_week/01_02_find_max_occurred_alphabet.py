# Q.  다음과 같은 문자열을 입력받았을 때,
# 어떤 알파벳이 가장 많이 포함되어 있는지 반환하시오.
# (단 최빈값을 가진 알파벳이 여러개일 경우
# 알파벳 순서가 가장 앞에 위치한 알파벳을 출력하시오)
# "hello my name is dingcodingco"

# [코드스니펫] 최빈값 찾기
# def find_max_occurred_alphabet(string):
#     # 이 부분을 채워보세요!
#     return "a"

# 내 아이디어 정리
# 1. map 자료구조를 사용해서 key 는 알파벳, value는 개수로 관리
# 2. value 가 가장 높은 값을 출력
# 3. 단 최빈값이 여러개일 경우를 찾으려면 어떻게 하는게 좋을지?

# 팁
# 1. 문자인지 확인하는 과정이 필요하다
# 파이썬의 내장 함수 str.isalpha() 를 이용해서 알파벳인지 확인할 수 있다.
# 2. 알파벳 별로 빈도수를 리스트에 저장하면 된다 map을 생각했지만 배열도 가능하다.
# 내장함수 ord() 를 이용해서 아스키 값을 통해 알파벳 순서대로 0번 부터 넣을 수 있게 한다.
# 3. 과정이 길다면 중간중간 print 를 찍어보면서 테스트하는 과정도 필요하다
def find_max_occurred_alphabet(string):
    # 알파벳 총 26개를 대상으로 각각의 개수를 저장할 배열을 만들어 둔다
    alphabet_occurrence_array = [0] * 26

    # 받아온 string 으로 부터 각 알파벳의 개수를 index에 맞춰 저장한다
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    # 배열의 길이만큼 for문을 돌며 가장 큰 개수가 들어있는 index를 찾는다
    max_occurrence = 0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence > max_occurrence:
            max_occurrence = alphabet_occurrence
            max_alphabet_index = index

    return chr(max_alphabet_index + ord('a'))

result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))