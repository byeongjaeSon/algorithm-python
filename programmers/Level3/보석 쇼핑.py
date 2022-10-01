from collections import defaultdict

def solution(gems):
    answer = []
    type_cnt = len(set(gems))
    
    l, r = 0, 1
    curr_gem = defaultdict(int)
    curr_gem[gems[l]] += 1
    
    while l < r:
        if len(curr_gem) < type_cnt and r < len(gems):
            curr_gem[gems[r]] += 1
            r += 1
        else:
            if len(curr_gem) == type_cnt:
                answer.append((l+1, r))
            
            curr_gem[gems[l]] -= 1
            if curr_gem[gems[l]] == 0:
                curr_gem.pop(gems[l], None)
        
            l += 1
            
    answer.sort(key = lambda x : (x[1] - x[0]))        
    
    return answer[0]
