# 프로그래머스 - 순위 검색(72412)
# https://school.programmers.co.kr/learn/courses/30/lessons/72412

from collections import defaultdict
import bisect

def solution(info, query):
    answer = [0] * len(query)
    condition_to_scores = defaultdict(list)
    
    for e in info:
        split_info = e.split(' ')
        condition_to_scores[tuple(split_info[:4])].append(int(split_info[4]))
    
    for scores in condition_to_scores.values():
        scores.sort()
    
    for i, q in enumerate(query):
        split_q = q.split(' ')
        threshold = int(split_q[7])
        q_condition = [split_q[i] for i in range(0, 7, 2) if split_q[i] != '-']
        
        for condition, scores in condition_to_scores.items():
            if all(map(lambda c : c in condition, q_condition)):
                answer[i] += len(scores) - bisect.bisect_left(scores, threshold)
        
    return answer
