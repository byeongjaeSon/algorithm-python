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
