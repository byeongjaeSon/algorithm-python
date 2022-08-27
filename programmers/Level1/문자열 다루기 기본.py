# 프로그래머스 - 문자열 다루기 기본(12918)
# https://school.programmers.co.kr/learn/courses/30/lessons/12918

def solution(s):
    return len(s) in (4,6) and s.isdigit()
