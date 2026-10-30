import heapq

class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :type k: int
        :rtype: int
        """

        # Build graph
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))

        INF = 10**30

        # dist[node][run]
        # run = number of consecutive equal labels ending at node
        dist = [[INF] * (k + 1) for _ in range(n)]

        # Node 0 is already visited, so its run length is 1
        dist[0][1] = 0

        # (cost, node, run)
        pq = [(0, 0, 1)]

        while pq:
            cost, u, run = heapq.heappop(pq)

            if cost != dist[u][run]:
                continue

            # Reached destination
            if u == n - 1:
                return cost

            for v, w in graph[u]:

                if labels[v] == labels[u]:
                    new_run = run + 1

                    # Cannot have more than k consecutive equal chars
                    if new_run > k:
                        continue
                else:
                    new_run = 1

                new_cost = cost + w

                if new_cost < dist[v][new_run]:
                    dist[v][new_run] = new_cost
                    heapq.heappush(
                        pq,
                        (new_cost, v, new_run)
                    )

        return -1