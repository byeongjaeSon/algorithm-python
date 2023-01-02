class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        all_path = []
        stack = [(0, [0])]
        dest = len(graph)-1
        
        while stack:
            curr_node, path = stack.pop()
            if curr_node == dest:
                all_path.append(path)
                continue
            
            for next_node in graph[curr_node]:
                stack.append((next_node, path+[next_node]))
                
        return all_path
