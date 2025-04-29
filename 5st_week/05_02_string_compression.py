# Q. 데이터 처리 전문가가 되고 싶은 어피치는 문자열을 압축하는 방법에 대해 공부를 하고 있습니다.
#
# 최근에 대량의 데이터 처리를 위한 간단한 비손실 압축 방법에 대해 공부를 하고 있는데,
# 문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현하는 알고리즘을 공부하고 있습니다.
#
# 간단한 예로 aabbaccc의 경우 2a2ba3c(문자가 반복되지 않아 한번만 나타난 경우 1은 생략함)와 같이 표현할 수 있는데,
# 이러한 방식은 반복되는 문자가 적은 경우 압축률이 낮다는 단점이 있습니다. 예를 들면, abcabcdede와 같은 문자열은 전혀 압축되지 않습니다.
# 어피치는 이러한 단점을 해결하기 위해 문자열을 1개 이상의 단위로 잘라서 압축하여 더 짧은 문자열로 표현할 수 있는지 방법을 찾아보려고 합니다.
#
# 예를 들어, ababcdcdababcdcd의 경우 문자를 1개 단위로 자르면 전혀 압축되지 않지만, 2개 단위로 잘라서 압축한다면 2ab2cd2ab2cd로 표현할 수 있습니다.
# 다른 방법으로 8개 단위로 잘라서 압축한다면 2ababcdcd로 표현할 수 있으며, 이때가 가장 짧게 압축하여 표현할 수 있는 방법입니다.
#
# 다른 예로, abcabcdede와 같은 경우, 문자를 2개 단위로 잘라서 압축하면 abcabc2de가 되지만,
# 3개 단위로 자른다면 2abcdede가 되어 3개 단위가 가장 짧은 압축 방법이 됩니다. 이때 3개 단위로 자르고 마지막에 남는 문자열은 그대로 붙여주면 됩니다.
#
# 압축할 문자열 input이 매개변수로 주어질 때, 위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라 압축하여
# 표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 string_compression 함수를 완성해주세요.
#
# * 문자열의 길이는 1 이상 1,000 이하입니다.
# * 문자열은 알파벳 소문자로만 이루어져 있습니다.
#
# 이 때, 문자열은 항상 제일 앞부터 정해진 길이만큼 잘라야 합니다.
# 입출력 예 #5 처럼 xababcdcdababcdcd 이 입력되어도,
# 문자열을 x / ababcdcd / ababcdcd 로 자르는 것은 불가능합니다.
# 이 경우 어떻게 문자열을 잘라도 압축되지 않으므로 가장 짧은 길이는 17이 됩니다.

# tip) 1 이상 1,000 이하 라는 조건이 주어지므로 이것은 입력값 N의 범위를 나타낸다
# 즉 N^2 일 떄는 1,000,000 이 될텐데 이 정도면 부하가 발생하지는 않는다
# N^3 은 무리다

# <문제분석>
# 문자열에서 같은 값이 연속해서 나타나는 것을 문자의 개수와 반복되는 값으료 표현
# 문자열을 1개 이상의 단위로 잘라서 압축하여 더 짧은 문자열로 표현
# 가장 짧게 압축하여 표현할 수 있는 방법? 단위가 클수록?
# *압축한 것 중 가장 짧은 것의 길이를 return 해야 한다!
# 1 <= string 길이 <= 1000
# 문자열은 알파벳 소문자로만 이루어져 있다
# *단, 문자열은 '항상' 제일 앞부터 정해진 길이만큼 잘라야 한다

# <문제풀이>
# 단, 문자열은 '항상' 제일 앞부터 정해진 길이만큼 잘라야 한다
# => 자를 수 있는 단위는 1부터 string의 길이 까지로 보면 된다?
# => 절반이 넘어가는 단위로 잘라봤자 반복되지 않으므로 *1부터 string 길이 / 2 까지만 반복
# 1. 같은 값이 연속 되어 나타나는 것을 어떻게 알 수 있을까?
# => 잘라봐야 알 수 있지 않을까?
# 2. 자를 수 있는 단위로 만들어지는 모든 경우의 수를 구해야 겠네
# 3. 그 결과들을 비교하여 가장 짧은 값의 길이를 출력해야 한다

# <코드변환>
# 1부터 문자열의 길이 / 2 까지 단위를 만들어서 단위를 1씩 늘리며 반복한다
# 단위 만큼 잘라서 앞의 것과 반복되면 숫자를 넣어 표현해주고 앞의 것과 최소 1번은 반복돼야 한다 반복을 못한다면 뒤에 이어 붙여줘야 한다
# 마지막에 비교해서 길이 값을 내놓아야 한다

input = "abcabcabcabcdededededede"

# n = len(input)
# for split_size in range(1, n // 2 + 1):  # 자르는 단위 반복
#     splited = [
#         input[i:i + split_size] for i in range(0, n, split_size)  # 아래 배열 안에 넣을 반복문을 파이썬에서는 이런식으로 넣을 수 있다
#     ]
#     # for i in range(0, n, split_size): # 문자열을 단위 만큼 자르기 위한 반복
#     #     print(i, input[i:i + split_size]) # !파이썬에서는 인덱스를 넘어가도 에러가 발생하지 않음 자체적으로 처리해 줌
#     #     splited.append(input[i:i + split_size])

def string_compression(string):
    n = len(string)
    result = n
    for split_size in range(1, n // 2 + 1): # 자르는 단위 반복
        splited = [
            string[i:i + split_size] for i in range(0, n, split_size) # 아래 배열 안에 넣을 반복문을 파이썬에서는 이런식으로 넣을 수 있다
        ]
        # print("splited : ", splited)
        compressed = ""
        count = 1 # 반복 개수
        for i in range(0, len(splited) - 1): # 앞에 것과 뒤에 것이 같은지 체크, 그러므로 맨 마지막 원소는 범위에서 제거
            cur, next = splited[i], splited[i + 1]

            if cur == next: # 반복 된다면
                count += 1
            else: # 더이상 반복되지 않는다면
                if count == 1:
                    compressed += cur # 반복되지 않았으므로 그냥 더한다
                else: # 반복 개수가 2 이상이면
                    compressed += f"{count}{cur}" # !파이썬에서 문자열을 합치는 방법
                count = 1

        # 마지막 원소에 대한 처리 => 여기가 중요하다!
        if count == 1: # 더이상 반복될 게 없었으므로
            compressed += splited[-1] # 맨 마지막 스트링 더해주기
        else: # 반복된 것 처리
            compressed += f"{count}{splited[-1]}"

        print("compressed : ", compressed)
        result = min(len(compressed), result)
    return result


print(string_compression(input))  # 14 가 출력되어야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA"))
print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA"))
print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))