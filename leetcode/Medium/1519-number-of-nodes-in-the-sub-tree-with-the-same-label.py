class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        self.ans = [0] * n
        adj_list = defaultdict(list)

        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        
        def dfs(node, parent):
            alphabet_counter = Counter([labels[node]])
            for adj_node in adj_list[node]:
                if adj_node == parent:    
                    continue
                alphabet_counter += dfs(adj_node, node)
            
            self.ans[node] = alphabet_counter[labels[node]]
            return alphabet_counter
        
        dfs(0, -1)
        return self.ans
