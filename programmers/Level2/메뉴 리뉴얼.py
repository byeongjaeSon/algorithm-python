from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    
    for menu_cnt in course:
        course_to_cnt = defaultdict(int)
        for order in orders:
            if len(order) < menu_cnt: continue
            combi = list(combinations(order, menu_cnt))
            for menu in combi:
                menu = sorted(menu, key = lambda x: x)
                course_to_cnt[''.join(menu)] += 1
                
        cnts = course_to_cnt.values()
        if not cnts: continue
        max_cnt = max(cnts)
        if max_cnt <= 1: continue
        for course, cnt in course_to_cnt.items():
            if cnt == max_cnt:
                answer.append(course)
                
    answer.sort()
    return answer
