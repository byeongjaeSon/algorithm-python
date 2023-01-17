class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        remainZeroCnt = s.count('0')
        metOneCnt = 0
        flipCnt = len(s) - remainZeroCnt
        for c in s:
            if c == '0':
                remainZeroCnt -= 1
            else:
                flipCnt = min(flipCnt, metOneCnt + remainZeroCnt)
                metOneCnt += 1
            
        return flipCnt
