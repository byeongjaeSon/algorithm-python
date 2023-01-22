class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret = set()
        partition = []
        def back_tracking(index):
            if index >= len(s):
                ret.add(tuple(partition))
                return

            for pos in range(index+1, len(s)+1):
                substring = s[index:pos]
                if len(substring) > 1 and (substring != substring[::-1]):
                    continue
                partition.append(substring)
                back_tracking(pos)
                partition.pop()

        back_tracking(0)
        return ret    
