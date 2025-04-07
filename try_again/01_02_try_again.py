# Q.  다음과 같은 문자열을 입력받았을 때,
# 어떤 알파벳이 가장 많이 포함되어 있는지 반환하시오.
# (단 최빈값을 가진 알파벳이 여러개일 경우
# 알파벳 순서가 가장 앞에 위치한 알파벳을 출력하시오)
# "hello my name is dingcodingco"

# 아이디머
# 1. 알파벳 문제니까 빈배열 size 26 개 생성
# 2. 개수를 저장해줘야함
# 3. 마지막에 반환할 때 알파벳으로 출력해야 함

def find_max_occurred_alphabet(string):
    alphabet_array = [0] * 26

    # 각 알파벳 개수 저장
    for char in string:
        if char.isalpha():
            index = ord(char) - ord('a')
            alphabet_array[index] += 1

    # 가장 큰 값이 있는 인덱스 찾기
    max_index = 0
    max_value = 0
    for i in range(len(alphabet_array)):
        value = alphabet_array[i]
        if max_value < value:
            max_value = value
            max_index = i

    # 그 인덱스를 알파벳으로 변환
    return chr(max_index + ord('a'))


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))