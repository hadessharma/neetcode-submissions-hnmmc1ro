class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for u, v in prerequisites:
            adj[u].append(v)
            in_degree[v] += 1
        
        q = deque()
        rem = numCourses

        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
                rem -= 1
        
        while q:
            node = q.popleft()

            for nei in adj[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)
                    rem -= 1
        
        return rem == 0