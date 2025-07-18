# Q. 택배 상자

# <문제분석>
# 택배상자는 크기가 모두 같고
# 1번 부터 n번 상자까지 번호가 증가하는 순서대로 일렬로 놓여 전달
# 한 방향으로만 진행 가능해서 1번부터 내릴 수 있다
# *하지만 알려준 순서에 맞게 택배 상자를 실어야 한다

# 맨 앞에 놓인 상자가 현재 트럭에 실어야 하는 순서가 아니면
# 그 상자를 트럭에 실을 순서가 될 때까지 다른 곳에 보관
# 다른 곳은 보조 컨테이너 벨트이고 이건 stack 으로 한 쪽에서만 뺄 수 있음

# ex. 5개 상자를 실어야 하며
# 알려준 순서가 4, 3, 1, 2, 5 순서라면
# 1, 2, 3을 보조에 넣고
# 4번은 트럭에 싣고
# 보조에서 3번 싣고
# 1번 실어야 하는데 꺼낼 수 없어서 포기
# 트럭에 2개의 상자만 실리게 된다

# 몇 개의 상자를 실을 수 있는지 return

# <풀이>
# 1. 1, len(order) + 1 만큼 돌면서
# 계속 돌아야 한다
# 2. 순서 맞으면 answer += 1 해주고 빼내고
# 순서 안맞으면 stack 에다가 보관
# 3. 순서 안맞으면 stack에서 마지막 값보며 확인하고 빼내주며 answer += 1

def solution(order):
    stack = []  # 보조 컨테이너
    idx = 0  # order에서 다음에 꺼내야 하는 상자 인덱스

    for n in range(1, len(order) + 1):
        if n == order[idx]:
            idx += 1
            # 기본 벨트 상자가 바로 원하는 상자라서 싣기
            # 싣고 나서 스택 검사하며 잔고 처리하기
            while stack and stack[-1] == order[idx]:
                stack.pop()
                idx += 1
        else:
            # 기본 벨트 상자가 원하는 순서가 아니면 보조 벨트에 저장
            stack.append(n)

    return idx

# <피드백>
# stack 에 보관하고 있는 것을 처리할 떄는
# while 문을 돌려 한 번에 처리 가능