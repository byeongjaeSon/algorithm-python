from collections import deque

def time_to_integer(time):
    hh, mm = time.split(":")
    return int(hh) * 60 + int(mm)
    
def integer_to_time(time):
    hh, mm = str(time//60), str(time%60)
    if len(hh) == 1:
        hh = "0" + hh
    if len(mm) == 1:
        mm = "0" + mm
    return hh + ":" + mm

def solution(n, t, m, timetable):
    answer = ''
    timetable = deque(sorted(list(map(time_to_integer, timetable))))  
    curr_time = time_to_integer("09:00")
    while n > 0:
        curr_q = [] 
        while len(curr_q) < m:
            if len(timetable) == 0:
                break

            if timetable[0] <= curr_time:
                curr_q.append(timetable.popleft())
            else:
                break  
                
        if n == 1:
            if len(curr_q) < m:
                answer = integer_to_time(curr_time)
            else:
                answer = integer_to_time(curr_q[-1]-1)
                     
        curr_time += t
        n -= 1
        
    return answer
