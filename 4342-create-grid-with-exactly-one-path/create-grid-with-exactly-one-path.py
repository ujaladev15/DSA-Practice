class Solution(object):
    def createGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: List[str]
        """
        grid = [['#'] * n for _ in range(m)]

        # Path: move right along first row
        for j in range(n):
            grid[0][j] = '.'

        # Then move down along last column
        for i in range(m):
            grid[i][n - 1] = '.'

        return [''.join(row) for row in grid]