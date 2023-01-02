class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        
        pattern_to_word = dict()
        word_to_pattern = dict()
        for w, p in zip(words, pattern):
            if p not in pattern_to_word:
                pattern_to_word[p] = w
            elif pattern_to_word[p] != w:
                return False
            
            if w not in word_to_pattern:
                word_to_pattern[w] = p
            elif word_to_pattern[w] != p:
                return False
            
        return True
