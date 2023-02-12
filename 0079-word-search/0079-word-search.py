class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        def find(i, j, pos = 0):
            if pos == len(word):
                return True
            if not(0 <= i < m) or not(0 <= j < n) or board[i][j] == "#":
                return False
            if board[i][j] == word[pos]:
                temp = board[i][j]
                board[i][j] = "#"
                if find(i, j-1, pos+1) or find(i, j+1, pos+1) or find(i-1, j, pos+1) or find(i+1, j, pos+1):
                    return True
                board[i][j] = temp
            return False
        for i in range(m):
            for j in range(n):
                if find(i ,j):
                    return True
        return False