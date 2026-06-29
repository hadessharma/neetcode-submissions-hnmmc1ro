from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 1. Condition for a valid tree: exact number of edges
        if len(edges) != n - 1:
            return False

        # 2. Build the adjacency list correctly
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        # 3. Simple DFS to find all connected nodes
        def dfs(node: int):
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)

        # 4. Start traversing from node 0
        dfs(0)

        # 5. If we visited all nodes, it's a single connected component (a valid tree)
        return len(visited) == n