import heapq
from collections import defaultdict

def solution(n, roads, sources, destination):
    INF = 1e8
    distance = [INF] * (n + 1)

    def dijkstra(start):
        pq = []
        heapq.heappush(pq, (0, start))
        distance[start] = 0

        while pq:
            dist, curr = heapq.heappop(pq)

            if distance[curr] < dist:
                continue

            for next in graph[curr]:
                if dist + 1 < distance[next]:
                    distance[next] = dist + 1
                    heapq.heappush(pq, (dist + 1, next))

    graph = defaultdict(list)
    for node1, node2 in roads:
        graph[node1].append(node2)
        graph[node2].append(node1)

    dijkstra(destination)

    result = [-1 if distance[source] == INF else distance[source] for source in sources]
    return result
