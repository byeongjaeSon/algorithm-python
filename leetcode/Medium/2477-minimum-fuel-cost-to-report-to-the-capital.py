class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adjList = defaultdict(list)
        for a, b in roads:
            adjList[a].append(b)
            adjList[b].append(a)
        
        self.fuel = 0
        def dfs(parent, curr):
            numOfRepresentative = 1
            for adjNode in adjList[curr]:
                if parent != adjNode:
                    numOfRepresentative += dfs(curr, adjNode)
            if curr != 0:
                self.fuel += ceil(numOfRepresentative / seats)
            return numOfRepresentative

        dfs(-1, 0)
        return self.fuel
