class Solution:
    def distinctNames(self, ideas: List[str]) -> int: 
        prefix_to_suffixes = defaultdict(set)
        valid_name_cnt = 0
        for idea in ideas:
            prefix_to_suffixes[idea[0]].add(idea[1:])

        for prefix1 in prefix_to_suffixes:
            for prefix2 in prefix_to_suffixes:
                if prefix1 != prefix2:
                    group1 = prefix_to_suffixes[prefix1] - prefix_to_suffixes[prefix2]
                    group2 = prefix_to_suffixes[prefix2] - prefix_to_suffixes[prefix1]
                    valid_name_cnt += len(group1) * len(group2)
        
        return valid_name_cnt
