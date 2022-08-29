# 프로그래머스 - 후보키(42890)
# https://school.programmers.co.kr/learn/courses/30/lessons/42890

from itertools import combinations

candidate_keys = []

def is_minimal(c):
    for candidate_key in candidate_keys:
        if set(candidate_key).issubset(set(c)):
            return False
    return True

def is_unique(relation, c):
    s = set()
    for r in relation:
        data = ''.join([r[i] for i in c])
        if data in s:
            return False
        s.add(data)
    return True

def solution(relation):
    colCnt = len(relation[0])
    combi = sum([list(combinations(range(colCnt), i+1)) for i in range(colCnt)], [])

    for c in combi:
        if is_minimal(c) and is_unique(relation, c):
            candidate_keys.append(c)
    
    return len(candidate_keys)
