
from bisect import bisect_left


class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        # Store:
        # (right, left, weight, original_index)
        arr = [
            (r, l, w, i)
            for i, (l, r, w) in enumerate(intervals)
        ]

        # Sort by right endpoint
        arr.sort()

        rights = [x[0] for x in arr]

        # prev[i] = number of intervals before i
        # whose right endpoint is strictly less than
        # arr[i].left
        prev = [0] * n

        for i in range(n):
            left = arr[i][1]
            prev[i] = bisect_left(rights, left, 0, i)

        # dp[k][i] = best result using at most k intervals
        # from the first i sorted intervals.
        #
        # Each state is:
        # (score, tuple_of_original_indices)
        dp = [
            [(0, ()) for _ in range(n + 1)]
            for _ in range(5)
        ]

        def better(a, b):
            # Higher score is better
            if a[0] != b[0]:
                return a if a[0] > b[0] else b

            # Same score -> lexicographically smaller indices
            return a if a[1] < b[1] else b

        for k in range(1, 5):
            for i in range(1, n + 1):

                # Option 1: don't take current interval
                best = dp[k][i - 1]

                # Option 2: take current interval
                idx = i - 1

                right, left, weight, original_index = arr[idx]

                old_score, old_indices = dp[k - 1][prev[idx]]

                candidate = (
                    old_score + weight,
                    tuple(sorted(old_indices + (original_index,)))
                )

                dp[k][i] = better(best, candidate)

        return list(dp[4][n][1])

