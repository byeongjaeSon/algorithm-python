class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:    
        degree = [0] * (n+1)
        for a, b in trust:
            degree[a] -= 1 # out-degree
            degree[b] += 1 # in-degree
        
        for i in range(1, n+1):
            if degree[i] == n-1:
                return i
        return -1
