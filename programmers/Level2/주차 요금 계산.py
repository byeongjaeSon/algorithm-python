from collections import defaultdict 
from math import ceil

def solution(fees, records):
    answer = []
    car_to_time = defaultdict(list)
    basic_time, basic_fee, unit_time, unit_fee = fees[0], fees[1], fees[2], fees[3]
    for record in records:
        r = record.split()
        time = r[0].split(":")
        car_to_time[r[1]].append((int(time[0]) * 60 + int(time[1])))
    
    for k, v in sorted(car_to_time.items()):
        parking_time = 0
        if len(v) % 2 == 1:
            v.append(23 * 60 + 59)
        for i in range(1, len(v), 2):
            parking_time += v[i] - v[i-1]
        
        answer.append(basic_fee)
        if parking_time > basic_time:
            answer[-1] += ceil((parking_time - basic_time) / unit_time) * unit_fee
    
    return answer
