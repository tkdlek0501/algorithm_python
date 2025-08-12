# Q. 스택 수열 (백준 1874, 실버2)

# 1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써,
# 하나의 수열을 만들 수 있다.
# 이때, 스택에 push 하는 순서는 반드시 오름차순을 지키도록 한다고 하자.
# 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지,
# 있다면 어떤 순서로 push 와 pop 연산을 수행해야 하는지를 알아낼 수 있다.
# 이를 계산하는 프로그램을 작성하라.

# 입력
# 첫 줄에 n (1 <= n < 100,000) 이 주어진다.
# 둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n 이하의 정수가
# 하나씩 순서대로 주어진다. 물론 같은 정수가 두 번 나오는 일은 없다.

# 출력
# 입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다.
# push 연산은 +로, pop 연산은 -로 표현하도록 한다.
# 불가능한 경우 NO를 출력한다.



# <문제풀이>
# 자료 구조 : stack
# 입력으로 임의의 수열이 주어짐 (둘째 줄부터 n개의 줄에 수열을 이루는 정수가 하나씩)
# stack 을 이용해서 그 수열을 만들어야 한다
# 만약 첫 줄에 8 이면 1 ~ 8
# 둘째 줄부터 나오는 수열을 만들려면?
# 1 2 3 4 5 6 7 8 을 가지고
# 4 3 6 8 7 5 2 1 얻으려면 어떻게?

# stack 에 있는 마지막 숫자와 얻으려는 숫자가 같은면 pop
# 아니면 push

def solution(n, arr): # 정수, 정수배열
    answer = [] # +, - 배열

    stack = []
    cur = 1
    for num in arr: # 얻고 싶은 배열 돌리면서
        while cur <= num: # 현재 숫자가 작으면
            stack.append(cur) # 그 숫자까지 넣어줌
            answer.append("+")
            cur += 1

        if stack and stack[-1] == num: # stack의 숫자가 얻고 싶은 숫자이면
            stack.pop() # 꺼냄
            answer.append("-")
        else: # 얻을 수 없으면 못만듦
            return ["NO"]

    return answer

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input().strip())
    arr = [int(input().strip()) for _ in range(n)]

    result = solution(arr)
    if result == ["NO"]:
        print("NO")
    else:
        print("\n".join(result))

# print(solution(8, [4, 3, 6, 8, 7, 5, 2, 1]))

# <피드백>
# 처음엔 while-pop 구조로 생각하고 풀었는데
# while-push 구조가 더 직관적인 느낌이 든다
# 필요한 숫자를 얻을 때까지 push 하고
# 그 이후 stack 을 돌며 필요한 숫자가 나오면 pop

# ex.
# 만약 4를 얻고 싶다면 while로 1, 2, 3, 4 넣어주고
# 마지막 4를 꺼내줌
# 다음 번에 큰 수 얻고 싶다고 하면 또 cur 보다 큰 수 while로 넣어주고
# 마지막 값 꺼내줌
# 작은 수 얻고 싶다고 하면 while 돌지 않고 stack 마지막 값인지 확인
# 여기서 값이 다르면 못만드는 수열이 됨
