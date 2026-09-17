class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)

        # best[i] = minimum length of a valid subarray
        # completely within arr[0...i]
        best = [float('inf')] * n

        left = 0
        curr_sum = 0
        ans = float('inf')

        for right in range(n):
            curr_sum += arr[right]

            # Since all numbers are positive,
            # shrink the window if sum becomes too large.
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            # Found a target-sum subarray [left...right]
            if curr_sum == target:
                length = right - left + 1

                # Find the best valid subarray before `left`
                if left > 0 and best[left - 1] != float('inf'):
                    ans = min(ans, length + best[left - 1])

                # Update best for this position
                if right == 0:
                    best[right] = length
                else:
                    best[right] = min(best[right - 1], length)

            else:
                # Carry forward the previous best
                if right > 0:
                    best[right] = best[right - 1]

        return -1 if ans == float('inf') else ans
        