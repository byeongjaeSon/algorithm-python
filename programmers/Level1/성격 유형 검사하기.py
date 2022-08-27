# 프로그래머스 - 성격 유형 검사하기(118666)
# https://school.programmers.co.kr/learn/courses/30/lessons/118666?

from collections import defaultdict

def solution(survey, choices):
    personality = ''
    indicators = [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N")]
    type_to_score = defaultdict(int)
    
    for s, c in zip(survey, choices):
        if c < 4:
            type_to_score[s[0]] += (4 - c)
        elif c > 4:
            type_to_score[s[1]] += (c - 4)
    
    for type1, type2 in indicators:
        if type_to_score[type1] < type_to_score[type2]:
            personality += type2
        else:
            personality += type1

    return personality
