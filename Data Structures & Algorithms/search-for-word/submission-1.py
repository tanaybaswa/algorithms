class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        """
        we have to do some sort of dfs from every cell
        """

        n = len(word)
        visited = set()
        d = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        max_i = len(board)
        max_j = len(board[0])

        def f(i, j, word_index):

            if word_index == n:
                return True

            for move in d:
                ni, nj = i + move[0], j + move[1]

                if 0 <= ni < max_i and 0 <= nj < max_j and (ni, nj) not in visited and board[ni][nj] == word[word_index]:

                    visited.add((ni, nj))

                    if f(ni, nj, word_index + 1):
                        return True

                    visited.remove((ni, nj))

        for i in range(max_i):
            for j in range(max_j):

                if board[i][j] == word[0]:
                    visited.add((i, j))
                    if f(i, j, 1):
                        return True
                    visited.remove((i, j))


        return False
        