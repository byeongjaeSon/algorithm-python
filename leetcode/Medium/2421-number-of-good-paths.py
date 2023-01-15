class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        adj_nodes = defaultdict(list)
        for v, u in edges:
            adj_nodes[v].append(u)
            adj_nodes[u].append(v)

        val_to_node = defaultdict(list)
        for node, val in enumerate(vals):
            val_to_node[val].append(node)

        def isGoodPath(parent, curr, dest):
            if curr == dest:
                return True
            
            if vals[curr] > vals[dest]:
                return False
            
            ret = False
            for adj_node in adj_nodes[curr]:
                if adj_node == parent:
                    continue
                ret = ret or isGoodPath(curr, adj_node, dest)            
            return ret
        
        good_path_cnt = 0
        for val, nodes in val_to_node.items():
            for i in range(len(nodes)):
                for j in range(i, len(nodes)):
                    good_path_cnt += isGoodPath(-1, nodes[i], nodes[j])

        return good_path_cnt
