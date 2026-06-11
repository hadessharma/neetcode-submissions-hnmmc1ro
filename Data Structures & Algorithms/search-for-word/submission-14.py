class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        res = False

        def dfs(i, j, idx):
            nonlocal res
            if res:
                return

            if idx == len(word):
                res = True
                return
            
            if (
                0 <= i < len(board) and
                0 <= j < len(board[i]) and
                board[i][j] == word[idx]
            ):
                board[i][j] = '#'
                dfs(i + 1, j, idx + 1)
                dfs(i - 1, j, idx + 1)
                dfs(i, j + 1, idx + 1)
                dfs(i, j - 1, idx + 1)

                board[i][j] = word[idx]
            
            return

        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, 0)
                if res:
                    return True
        
        return res