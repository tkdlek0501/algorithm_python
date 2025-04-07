# Q.
# 0과 1로만 이루어진 문자열이 주어졌을 때, 이 문자열에 있는 모든 숫자를 전부 같게 만들려고 한다.
# 할 수 있는 행동은 문자열에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다.
# 뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다.
#
# 예를 들어 S=0001100 일 때,
#
# 전체를 뒤집으면 1110011이 된다.
# 4번째 문자부터 5번째 문자까지 뒤집으면 1111111이 되어서 2번 만에 모두 같은 숫자로 만들 수 있다.
# 하지만, 처음부터 4번째 문자부터 5번째 문자까지 문자를 뒤집으면 한 번에 0000000이 되어서 1번 만에 모두 같은 숫자로 만들 수 있다.
#
# 주어진 문자열을 모두 0 혹은 모두 1로 같게 만드는 최소 횟수를 반환하시오.


input = "011110"

# 아이디어
# 언제 0에서 1로 변하는지 1에서 0으로 변하는지가 뒤집는 타이밍이다.
# 0에서 1로 변할 때 뒤집을지(전체를 0으로), 1에서 0으로 변할 때 뒤집을지(전체를 1로)
# 0을 1로 뒤집는 횟수 vs 1을 0으로 뒤집는 횟수

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0
    count_to_all_one = 0

    # 맨 첫번째 숫자는 무조건 뒤집는 것으로 생각
    if string[0] == '0':
        count_to_all_one += 1
    elif string[0] == '1':
        count_to_all_zero += 1

    for i in range(len(string) - 1): # i 는 0부터 문자열의 길이 - 2 -> 앞에 거와 뒤에 거를 비교해야하므로 맨 마지막 문자 이 전까지만 반복
        if string[i] != string[i + 1]: # 앞의 숫자와 뒤의 숫자가 다르면 뒤집는 타이밍
            if string[i + 1] == "1": # 앞은 0이고 뒤는 1이라면
                count_to_all_zero += 1 # 뒤의 숫자를 1로
            if string[i + 1] == "0":
                count_to_all_one += 1
    print(count_to_all_zero)
    print(count_to_all_one)

    return min(count_to_all_zero, count_to_all_one)

result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)