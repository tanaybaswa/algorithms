class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:


        n = len(text1)
        m = len(text2)

        matrix = [[0] * (m + 1) for _ in range(n + 1)]

        output = 0


        for i in range(1, n + 1):
            c1 = text1[i - 1]
            
            for j in range(1, m + 1):
                c2 = text2[j - 1]

                top = matrix[i - 1][j]
                left = matrix[i][j - 1]
                topleft = matrix[i - 1][j - 1]

                match = int(c1 == c2)

                potential = max(top, left, topleft + match)

                matrix[i][j] = potential

        print(matrix)

        return matrix[n][m]



        