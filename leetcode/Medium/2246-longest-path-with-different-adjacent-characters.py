class Solution:
    def longestPath(self, parent, s):
        children_nodes = defaultdict(list)
        for c, p in enumerate(parent):
            if p < 0:
               continue
            children_nodes[p].append(c)
        
        self.global_longest_path = 1
        def dfs(node):
            path_chain_1 = path_chain_2 = 0
            for child_node in children_nodes[node]:
                candi = dfs(child_node)
                
                if s[node] == s[child_node]:
                    continue
                
                if candi > path_chain_1:
                    path_chain_2 = path_chain_1
                    path_chain_1 = candi
                elif candi > path_chain_2:
                    path_chain_2 = candi

            local_longest_path = path_chain_1 + path_chain_2 + 1
            self.global_longest_path = max(self.global_longest_path, local_longest_path)
            return path_chain_1 + 1

        dfs(0)
        return self.global_longest_path
