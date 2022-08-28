# 프로그래머스 - [3차]압축(17684)
# https://school.programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    answer = []
    dic = {chr(ord('A') + i): i + 1 for i in range(26)}
    l, r = 0, 1
    while r < len(msg):
        if msg[l:r + 1] not in dic:
            answer.append(dic[msg[l:r]])
            dic[msg[l:r + 1]] = len(dic) + 1
            l = r
        r += 1
    answer.append(dic[msg[l:]])
    return answer
