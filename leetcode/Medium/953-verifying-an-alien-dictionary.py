class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_to_order = {order[i] : i for i in range(len(order))}
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j >= len(words[i+1]):
                    return False
                if words[i][j] != words[i+1][j]:
                    if char_to_order[words[i][j]] > char_to_order[words[i+1][j]]:
                        return False
                    break
        return True
