class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj: List[List[int]] = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited: Set[int] = set()

        def dfs(par: int, node: int):          
            if node in visited:
                return False

            visited.add(node)

            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(node, nei):
                    return False

            return True
        
        if not dfs(-1, 0):
            return False
        
        return len(visited) == n