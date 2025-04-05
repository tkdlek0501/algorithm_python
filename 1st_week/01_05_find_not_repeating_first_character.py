# Q. 다음과 같이 영어로 되어 있는 문자열이 있을 때,
# 이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오.
# 만약 그런 문자가 없다면 _ 를 반환하시오.

#"abadabac"
# 반복되지 않는 문자는 d, c 가 있지만
# "첫번째" 문자니까 d를 반환해주면 됩니다!

# 아이디어
def find_not_repeating_first_character(string):
    # 1. 각 알파벳이 몇 개가 나왔는지 확인 필요 -> array 에 알파벳 순서대로 개수 대입
    alpabet_array = [0] * 26
    for char in string:
        index = ord(char) - ord('a')
        alpabet_array[index] += 1

    # 2. 반복되지 않은 알파벳만 추출 == 개수가 1개 인것만
    not_repeat_array = []
    for index in range(len(alpabet_array)):
        if alpabet_array[index] == 1:
            not_repeat_array.append(chr(index + ord("a")))

    # 3. 첫번째 문자를 반환 -> 받아온 string 과 비교하여 있는 값 바로 반환
    for char in string:
        if char in not_repeat_array:
            return char
    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 = _ 현재 풀이 값 =", result("aaaaaaaa"))