"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        mp = {}

        q = deque()
        q.append(node)

        visited = set()

        while q:
            curr = q.popleft()

            if curr not in mp:
                mp[curr] = Node(curr.val)
            if curr in visited:
                continue
            visited.add(curr)
            clone = mp[curr]
            for nei in curr.neighbors:
                q.append(nei)
                if nei not in mp:
                    mp[nei] = Node(nei.val)
                clone.neighbors.append(mp[nei])

        return mp[node]



        