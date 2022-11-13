def solution(n, s):
    if s < n:
        return [-1]
    
    answer = [s//n for _ in range(n)]
    
    for i in range(s % n):
        answer[-1-i] += 1
        
    return answer
