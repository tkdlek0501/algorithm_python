# Q. 오픈채팅방

# <문제분석>
# 들어오고, 나가는 것을 볼 수 있는 관리자 창
# 누군가 들어오면
# "[닉네임]님이 들어왔습니다."
# 누군가 나가면
# "[닉네임]님이 나갔습니다."

# 닉네임을 변경하는 방법은 두 가지
# 1. 채팅방 나간 후, 새로운 닉네임으로 다시 들어간다.
# 2. 채팅방에서 닉네임을 변경한다.
# 닉네임 변경 시 기존 채팅방에 출력되어 있던 메시지의 닉네임도 전부 변경됨
# 채팅방은 중복 닉네임을 허용

# 채팅방에 들어오고 나가거나, 닉네임을 변경한 기록이 담긴 문자열 배열 records
# 최종적으로 방을 개설한 사람이 보게 되는 메시지를 문자열 배열 형태로 return
# records 는 100,000 이하
# 들어오면 "Enter [유저 아이디] [닉네임]"
# 나가면 "Leave [유저 아이디] [닉네임]"
# 닉네임 변경 시 "Change [유저 아이디] [닉네임]"

# <풀이>
# 들어오고 나간 기록을 순서대로 기록해야 한다
# 배열로 들어오고 나간 기록 쌓아놓고 (user_id, status) 튜플로
# dic 로 user_id 에 해당하는 닉네임 따로 관리
# 마지막에 다시 배열 for문 돌아서 처리

def solution(record):
    answer = []

    records = []  # [(user_id, status), ...]
    dic = {}  # dic[유저아이디] = 닉네임

    for rec in record:
        r = rec.split()
        if r[0] == 'Enter':
            records.append((r[1], r[0]))
            dic[r[1]] = r[2]
        elif r[0] == 'Leave':
            records.append((r[1], r[0]))
        else:  # Change
            dic[r[1]] = r[2]

    for rec in records:  # 출입기록 돌면서
        user_id, status = rec[0], rec[1]
        if status == 'Enter':
            answer.append(dic[user_id] + "님이 들어왔습니다.")
        else:  # Leave
            answer.append(dic[user_id] + "님이 나갔습니다.")

    return answer