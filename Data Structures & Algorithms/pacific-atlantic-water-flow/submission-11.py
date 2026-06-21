class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        atl = [[False for _ in range(COLS)] for __ in range(ROWS)]
        pac = [[False for _ in range(COLS)] for __ in range(ROWS)]


        def bfs(r, c, ocean):
            q = deque([(r, c)])
            ocean[r][c] = True
            
            while q:
                x, y = q.popleft()

                for d1, d2 in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nr, nc = x + d1, y + d2

                    if (
                        nr < 0 or nr >= ROWS or
                        nc < 0 or nc >= COLS or
                        ocean[nr][nc] or
                        heights[nr][nc] < heights[x][y]
                    ):
                        continue

                    ocean[nr][nc] = True
                    q.append((nr, nc))
        
        to_process = []

        # top, bottom        
        for r in range(ROWS):
            to_process.append([r, 0, pac])
            to_process.append([r, COLS - 1, atl])

        # left, right
        for c in range(COLS):
            to_process.append([0, c, pac])
            to_process.append([ROWS - 1, c, atl])

        for r, c, ocean in to_process:
            bfs(r, c, ocean)
        
        res = []
    
        for r in range(ROWS):
            for c in range(COLS):
                if atl[r][c] and pac[r][c]:
                    res.append([r, c])

        return res