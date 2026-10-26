class Solution(object):
    def countIslands(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        visited = [[False] * n for _ in range(m)]
        ans = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(m):
            for j in range(n):

                if grid[i][j] == 0 or visited[i][j]:
                    continue

                stack = [(i, j)]
                visited[i][j] = True
                total = 0

                while stack:
                    x, y = stack.pop()
                    total += grid[x][y]

                    for dx, dy in directions:
                        nx = x + dx
                        ny = y + dy

                        if (0 <= nx < m and
                            0 <= ny < n and
                            grid[nx][ny] > 0 and
                            not visited[nx][ny]):

                            visited[nx][ny] = True
                            stack.append((nx, ny))

                if total % k == 0:
                    ans += 1

        return ans