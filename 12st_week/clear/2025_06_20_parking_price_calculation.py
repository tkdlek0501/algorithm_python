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

from collections import defaultdict

def solution1(fees, records):  # 주차요금 정수배열, 자동차 입/출차 내역
    answer = []

    default_time, default_price, unit_time, unit_price = fees

    def convert_time(t):
        hour, minute = t.split(':')
        return int(hour) * 60 + int(minute)

    in_records = {}  # 차량번호 : 입차 시각
    time_records = defaultdict(int)  # 차량번호 : 누적 시간
    for record in records:
        time, number, status = record.split()
        if status == 'IN':
            in_records[number] = time
        else:
            in_time = in_records[number]  # 입차 시간
            del in_records[number]  # 기록 제거
            in_t = convert_time(in_time)
            out_t = convert_time(time)
            time_records[number] += (out_t - in_t)

    last_t = convert_time("23:59")
    if in_records:  # 출차 안된 차 있으면
        for record in in_records:
            in_t = convert_time(in_records[record])
            time_records[record] += (last_t - in_t)

    # 요금 계산
    result_dict = {}
    for record in time_records:  # 차량번호, 누적시간
        if time_records[record] <= default_time:  # 기본 시간 이하
            result_dict[record] = default_price  # 기본 요금만
        else:
            exceed_t = (time_records[record] - default_time)  # 초과시간
            unit = 0
            if exceed_t % unit_time != 0:
                unit = (exceed_t // unit_time + 1)  # 올림
            else:
                unit = exceed_t // unit_time
            exceed_price = unit * unit_price  # 초과 금액
            result_dict[record] = (default_price + exceed_price)
    # print(result_dict)

    res = sorted(result_dict)
    for r in res:
        answer.append(result_dict[r])

    return answer

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
# 어떻게 푸는지 알고 막힘 없이 푸는데도 30분 이상 걸리는 구현 문제

# 어떤 정보를 어떤 자료구조로 관리할지 파악하고 풀어나가면 된다
# 예외 처리에 대해서 신경써야 한다

# import math 를 통해
# math.ceil() 로 올림 처리 가능
# -(-exceed_t // unit_time)  # -값으로 올림 나눗셈 방식도 가능

# map(int, time_str.split(":")) 처럼 map(자료형, 대상리스트) 문법