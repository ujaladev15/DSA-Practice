class Solution(object):
    def rotateTheBox(self, boxGrid):
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """
        m = len(boxGrid)
        n = len(boxGrid[0])

        # Make stones fall toward the right
        for r in range(m):
            empty = n - 1

            for c in range(n - 1, -1, -1):
                if boxGrid[r][c] == '*':
                    empty = c - 1

                elif boxGrid[r][c] == '#':
                    boxGrid[r][c] = '.'
                    boxGrid[r][empty] = '#'
                    empty -= 1

        # Rotate 90 degrees clockwise
        result = [['.'] * m for _ in range(n)]

        for r in range(m):
            for c in range(n):
                result[c][m - 1 - r] = boxGrid[r][c]

        return result