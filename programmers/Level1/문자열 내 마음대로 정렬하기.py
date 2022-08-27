# 프로그래머스 - 문자열 내 마음대로 정렬하기(12925)
# https://school.programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    strings.sort(key = lambda x : (x[n], x))
    return strings
