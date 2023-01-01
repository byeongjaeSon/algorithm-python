class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        
        pattern_to_word = dict()
        word_to_pattern = dict()
        for i in range(len(pattern)):
            if pattern[i] not in pattern_to_word:
                pattern_to_word[pattern[i]] = words[i]
            elif pattern_to_word[pattern[i]] != words[i]:
                return False

            if words[i] not in word_to_pattern:
                word_to_pattern[words[i]] = pattern[i]
            elif word_to_pattern[words[i]] != pattern[i]:
                return False
            
        return True
