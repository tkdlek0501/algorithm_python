# Q. 주차 요금 계산

# <문제분석>
# 주차장 요금표
# 입차, 출차 기록 주어진다
# 차량별로 주차 요금을 계산하려고 한다

# 기본 요금이 있고 다위 요금이 있다
# 차량번호가 있고 입차 출차 시간이 있다
# 한 차량이 여러번 입차 가능하다

# 주차 요금을 나타내는 정수 배열 fees
# 자동차의 입/출차 내역을 나타내는 문자열 배열 records 주어지면
# 차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에 담아서 return

# fees의 길이는 4
# fees[0] = 기본 시간(분)
# fees[1] = 기본 요금
# fees[2] = 단위 시간
# fees[3] = 단위 요금
# 기본요금 + ((경과시간 - 기본시간) / 10) x 600 = 주차 요금
# 경과시간이 기본 시간보다 작으면 기본 요금만 주차 요금

# <풀이>
# 1. 차량번호가 작은 순으로 return 해야 하므로 dic으로 뽑아낸다
# dic 은 차량번호, 주차요금으로 관리
# 2. records(길이 1000 이하) for 문 돌아서
# 3. 하나씩 꺼내서 split 해서 기록해야 한다
#  입차가 됐을 때 배열에 넣고 출차 됐을 때 꺼내서 요금 계산
# 23:59 분까지 출차 안되면 23:59 로 계산

import math
from collections import defaultdict

def time_to_minutes(time_str): # 시간 -> 분 변환
    h, m = map(int, time_str.split(":"))
    return h * 60 + m

def solution(fees, records):
    base_time, base_fee, unit_time, unit_fee = fees
    in_records = {} # 입차시간 기록
    total_times = defaultdict(int)

    for record in records:
        time_str, car_num, status = record.split()
        time = time_to_minutes(time_str)
        if status == 'IN':
            in_records[car_num] = time
        else:  # OUT
            in_time = in_records.pop(car_num) # 입차시간 기록 제거
            total_times[car_num] += time - in_time

    # 출차 안 된 차량 처리 (23:59 출차 간주)
    end_of_day = time_to_minutes("23:59")
    for car_num, in_time in in_records.items():
        total_times[car_num] += end_of_day - in_time

    # 요금 계산
    result = []
    for car_num in sorted(total_times.keys()):
        total_time = total_times[car_num]
        if total_time <= base_time:
            fee = base_fee
        else:
            extra_time = total_time - base_time
            fee = base_fee + math.ceil(extra_time / unit_time) * unit_fee
        result.append(fee)

    return result

# <피드백>
# 단순 구현 문제이나
# 관리해야 하는 포인트가 많고
# 특이 케이스(출차 시간 없을 경우 23:59 로 계산) 가 있어서
# 시간이 많이 필요한 문제

# total_times = defaultdict(int)
# defaultdict의 사용법 숙지
# dict.pop(key) 로 dict도 pop이 가능하다는 점 알고 있어야 한다

# 또한 문자열 파싱도 생각하지 않고 바로 튀어나올 수 있게 암기해놓자
# def time_to_minutes(time_str): # 시간 -> 분 변환
#     h, m = map(int, time_str.split(":"))
#     return h * 60 + m