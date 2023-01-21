class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ret = set()
        possibleIP = []
        def makePossibleIP(index):
            if len(possibleIP) == 4:
                if index >= len(s):
                    ret.add('.'.join(possibleIP))
                return

            for size in range(1,4):
                if index >= len(s):
                    break
                chunk = s[index:index+size]
                if len(chunk) > 1 and chunk[0] == '0':
                    continue
                if int(chunk) > 255:
                    continue

                possibleIP.append(chunk)
                makePossibleIP(index+size)
                possibleIP.pop()
        
        makePossibleIP(0)
        return list(ret)
