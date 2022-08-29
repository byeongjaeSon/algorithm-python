# 프로그래머스 - [1차] 뉴스 클러스터링(17677)
# https://school.programmers.co.kr/learn/courses/30/lessons/17677

from collections import Counter

def solution(str1, str2):
    l1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    l2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    if not l1 and not l2: 
        return 65536
    
    c1, c2 = Counter(l1), Counter(l2)
    return int((sum((c1&c2).values()) / sum((c1|c2).values()) * 65536))
