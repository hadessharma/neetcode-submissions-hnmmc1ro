from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        ROWS, COLS = len(heights), len(heights[0])

        pac = [[False for _ in range(COLS)] for _ in range(ROWS)]
        atl = [[False for _ in range(COLS)] for _ in range(ROWS)]

        q_pac = deque()
        q_atl = deque()

        # Seed the queues with border cells and mark them as visited (True) immediately
        for r in range(ROWS):
            pac[r][0] = True
            q_pac.append((r, 0))
            
            atl[r][COLS - 1] = True
            q_atl.append((r, COLS - 1))

        for c in range(COLS):
            pac[0][c] = True
            q_pac.append((0, c))
            
            atl[ROWS - 1][c] = True
            q_atl.append((ROWS - 1, c))

        # Helper function to run multi-source BFS
        def bfs(q, ocean):
            while q:
                x, y = q.popleft()

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = x + dx, y + dy

                    # Check boundaries, if it's already visited, and if water can flow 'up' to it
                    if (
                        nr < 0 or nr >= ROWS or 
                        nc < 0 or nc >= COLS or 
                        ocean[nr][nc] or 
                        heights[nr][nc] < heights[x][y]
                    ):
                        continue

                    ocean[nr][nc] = True
                    q.append((nr, nc))

        # Run BFS exactly twice
        bfs(q_pac, pac)
        bfs(q_atl, atl)
        
        # Find the intersection
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if atl[r][c] and pac[r][c]:
                    res.append([r, c])

        return res