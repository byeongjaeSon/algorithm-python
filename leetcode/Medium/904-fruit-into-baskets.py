class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, r = 0, 1 
        types = defaultdict(int)
        types[fruits[0]] += 1
        max_fruits = 1
        while l < r and r < len(fruits):
            types[fruits[r]] += 1
            if len(types.keys()) > 2:
                max_fruits = max(max_fruits, r - l)
                while len(types.keys()) > 2:
                    types[fruits[l]] -= 1
                    if types[fruits[l]] == 0:
                        del types[fruits[l]]
                    l += 1
            r += 1
        return max(max_fruits, r - l)
