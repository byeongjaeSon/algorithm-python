class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        char_cnt = 1
        for i in range(1, n):
            if chars[i-1] != chars[i]:                
                chars.append(chars[i-1])
                if char_cnt > 1:
                    for c in str(char_cnt):
                        chars.append(c)
                    char_cnt = 1
            else:
                char_cnt += 1
                
        chars.append(chars[n-1])
        if char_cnt > 1:
            for c in str(char_cnt):
                chars.append(c)
       
        for _ in range(n):
            chars.pop(0)

        return len(chars)