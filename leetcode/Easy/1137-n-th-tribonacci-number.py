class Solution:
    def tribonacci(self, n: int) -> int:
        seq = deque([0, 1, 1])
        if n < 3:
            return seq[n]
        
        for k in range(3, n+1):
            seq.append(sum(seq))
            seq.popleft()
        return seq[-1]
