# 프로그래머스 - [3차] 방금그곡(17683)
# https://school.programmers.co.kr/learn/courses/30/lessons/17683

def convert_sharp_to_lower(s):
    s = s.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    return s

def solution(m, musicinfos):
    candidates = []
    m = convert_sharp_to_lower(m)
    for musicinfo in musicinfos:
        info = musicinfo.split(',')
        play_time, title, sheet = (int(info[1][0:2])*60+int(info[1][3:])) - (int(info[0][0:2])*60+int(info[0][3:])), info[2], convert_sharp_to_lower(info[3]) 
        played_sheet = sheet * (play_time // len(sheet)) + sheet[:(play_time % len(sheet))]
        if m in played_sheet:
            candidates.append((title, play_time)) 
    
    if candidates:
        candidates.sort(key = lambda x : x[1], reverse=True)
        return candidates[0][0]
    else:
        return "(None)"
