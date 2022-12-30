class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ret = []
        n = len(graph)-1
        def dfs(curr_node, adjacent_nodes, path):
            new_path = path.copy()
            new_path.append(curr_node)
            if curr_node == n:
                ret.append(new_path)
            for next_node in adjacent_nodes:
                dfs(next_node, graph[next_node], new_path)

        dfs(0, graph[0], [])
        return ret
