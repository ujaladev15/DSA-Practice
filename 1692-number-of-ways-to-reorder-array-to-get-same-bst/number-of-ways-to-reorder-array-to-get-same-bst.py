class Solution(object):
    def numOfWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute combinations
        C = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            C[i][0] = C[i][i] = 1
            for j in range(1, i):
                C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD

        def solve(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]

            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            left_ways = solve(left)
            right_ways = solve(right)

            ways = C[len(left) + len(right)][len(left)]
            ways = ways * left_ways % MOD
            ways = ways * right_ways % MOD

            return ways

        return (solve(nums) - 1) % MOD