from itertools import combinations_with_replacement
from functools import cmp_to_key

# https://stackoverflow.com/questions/5213033/sort-a-list-of-lists-with-a-custom-compare-function
def compare(a, b):
    for i in range(len(a[1])-1, -1, -1):
        if a[1][i] > b[1][i]:
            return -1
        elif a[1][i] == b[1][i]:
            continue
        else:
            return 1

def solution(n, info):
    candidate = []
    points = [point for point in range(11)]
    for cwr in combinations_with_replacement(points, n):
        rion_result = [0] * 11
        for point in cwr:
            rion_result[10 - point] += 1
        
        apache_score = rion_score = 0
        for i in range(11):
            if info[i] == rion_result[i] and info[i] == 0: continue
            if info[i] >= rion_result[i]: apache_score += 10 - i
            else: rion_score += 10 - i 
        
        if rion_score <= apache_score: continue
        
        score_diff = rion_score - apache_score
        if candidate:
            if score_diff > candidate[0][0]:
                candidate = [(score_diff, rion_result)]
            elif score_diff == candidate[0][0]:
                candidate.append((score_diff, rion_result))
        else:   
            candidate.append((score_diff, rion_result))
    
    if candidate:
        candidate.sort(key = cmp_to_key(compare))
        return candidate[0][1]
    else:
        return [-1]
